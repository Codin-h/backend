import random
from pprint import pprint

from world.PossibleWorldBlock import PossibleWorldBlock
from world.WorldBlock import WorldBlock
from world.enums.Directions import Directions
from world.consts.Others import directions

class World:
    def __init__(self, size: tuple[int, int, int] = (10, 1, 10)):
        self.X, self.Y, self.Z = size
        self.placed = {}  # coord -> WorldBlock
        self.frontier: dict[tuple[int,int,int], PossibleWorldBlock] = {}
        self._init_world()

    def _init_world(self):
        """
        Initialize with a random starting block and populate frontier.
        """
        start = (
            random.randint(0, self.X - 1),
            random.randint(0, self.Y - 1),
            random.randint(0, self.Z - 1)
        )
        block_type, subtype, rot = PossibleWorldBlock().collapse()
        wb = WorldBlock(rot, start, block_type, subtype)
        self.placed[start] = wb
        # add neighbors to frontier
        for n in self._get_neighbours(start):
            self.frontier[n] = PossibleWorldBlock()

    def generate_world(self):
        """
        Run collapse until all reachable positions are filled.
        """
        while self.frontier:
            # print("Frontier, Placed:")
            # pprint(self.frontier)
            # pprint(self.placed)

            # pick cell with lowest entropy
            coord, pwb = min(self.frontier.items(), key=lambda item: item[1].get_entropy())
            # print(f"Collapsing block at {coord} with entropy {pwb.get_entropy()}")

            # update possibilities based on placed neighbors
            for dx, dy, dz in directions:
                nbr = (coord[0] + dx, coord[1] + dy, coord[2] + dz)
                if nbr in self.placed:
                    # get rules from neighbor pointing towards coord
                    incoming = Directions.get_direction_from_A_to_B(nbr, coord)
                    rules = self.placed[nbr].get_building_rules(incoming)
                    if incoming == Directions.TOP or incoming == Directions.BOTTOM:
                        continue
                    pwb.update(rules)

            # collapse the block
            btype, subtype, rot = pwb.collapse()
            wb = WorldBlock(rot, coord, btype, subtype)
            self.placed[coord] = wb
            del self.frontier[coord]

            # add new neighbors to frontier
            for n in self._get_neighbours(coord):
                if n not in self.placed and n not in self.frontier:
                    self.frontier[n] = PossibleWorldBlock()

    def _get_neighbours(self, coord: tuple[int, int, int]) -> list[tuple[int,int,int]]:
        """
        Returns valid neighboring coordinates within bounds.
        """
        x,y,z = coord
        out = []
        for dx,dy,dz in directions:
            nx, ny, nz = x+dx, y+dy, z+dz
            if 0 <= nx < self.X and 0 <= ny < self.Y and 0 <= nz < self.Z:
                out.append((nx,ny,nz))
                # print(f"Adding neighbor: {nx, ny, nz}")
        return out

if __name__ == "__main__":
    world = World((100, 1, 100))
    world.generate_world()

    # Print final world state
    print("Final World Blocks:")
    pprint(world.placed)