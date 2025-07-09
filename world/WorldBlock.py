from copy import deepcopy
from pprint import pprint

from enums import Directions
from world.consts.Rules import *

class WorldBlock:
    def __init__(self, rotation: Rotations, coord: tuple[int, int, int], world_block_type: WorldBlockTypes, subtype:str):
        self.rotation = rotation
        self.coord = coord
        self.world_block_type = world_block_type
        self.subtype = subtype

    def get_building_rules(self, direction: Directions):
        """
        Returns the building rule in the given direction, accounting for block rotation.
        """
        base_rules = world_rules[self.world_block_type]
        rotated_rules = self._rotate_rules(self.rotation.value, base_rules)
        return rotated_rules.get(direction)

    def _rotate_rules(self, steps: int, rules_dict: dict) -> dict:
        """
        Rotates the rules dictionary counterclockwise by 90 degrees 'steps' times.
        """
        rules = deepcopy(rules_dict)
        for _ in range(steps):
            rules = self._rotate90_ccw(rules)
        return rules

    @staticmethod
    def _rotate90_ccw(rules_dict: dict) -> dict:
        """
        Rotates the direction keys in the rules dictionary 90 degrees counter-clockwise.
        """
        rotation_map = {
            Directions.NORTH: Directions.WEST,
            Directions.WEST: Directions.SOUTH,
            Directions.SOUTH: Directions.EAST,
            Directions.EAST: Directions.NORTH,
            Directions.TOP: Directions.TOP,
            Directions.BOTTOM: Directions.BOTTOM
        }

        return {rotation_map.get(dir_, dir_): val for dir_, val in rules_dict.items()}

    def __repr__(self):
        return f"WorldBlock(coord={self.coord}, type={self.world_block_type.name}, subtype={self.subtype}, rotation={self.rotation.name})"