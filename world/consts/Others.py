from world.enums.Rotations import Rotations
from world.enums.WorldBlockTypes import WorldBlockTypes

directions = [
    (1, 0, 0), # right
    (-1, 0, 0), # left
    (0, 0, 1), # front
    (0, 0, -1), # back
    (0, 1, 0), # top
    (0, -1, 0) # bottom
]

possible_blocks = {
    WorldBlockTypes.BUILDINGS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
    WorldBlockTypes.ROADS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
    WorldBlockTypes.CORNERS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
    WorldBlockTypes.JUNCTIONS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
    WorldBlockTypes.INTERSECTIONS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI]
}