from world.enums.Directions import Directions
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

# Direction mapping for rotations (world direction → original direction)
DIRECTION_MAP = {
    Rotations.ZERO: {
        Directions.SOUTH: Directions.SOUTH,
        Directions.NORTH: Directions.NORTH,
        Directions.WEST: Directions.WEST,
        Directions.EAST: Directions.EAST
    },
    Rotations.HALF_PI: {
        Directions.SOUTH: Directions.WEST,
        Directions.WEST: Directions.NORTH,
        Directions.NORTH: Directions.EAST,
        Directions.EAST: Directions.SOUTH
    },
    Rotations.PI: {
        Directions.SOUTH: Directions.NORTH,
        Directions.WEST: Directions.EAST,
        Directions.NORTH: Directions.SOUTH,
        Directions.EAST: Directions.WEST
    },
    Rotations.NEGATIVE_HALF_PI: {
        Directions.SOUTH: Directions.EAST,
        Directions.WEST: Directions.SOUTH,
        Directions.NORTH: Directions.WEST,
        Directions.EAST: Directions.NORTH
    }
}

# Rotation addition rules (current rotation + relative rotation → absolute rotation)
ROTATION_ADD = {
    Rotations.ZERO: {
        Rotations.ZERO: Rotations.ZERO,
        Rotations.HALF_PI: Rotations.HALF_PI,
        Rotations.PI: Rotations.PI,
        Rotations.NEGATIVE_HALF_PI: Rotations.NEGATIVE_HALF_PI
    },
    Rotations.HALF_PI: {
        Rotations.ZERO: Rotations.HALF_PI,
        Rotations.HALF_PI: Rotations.PI,
        Rotations.PI: Rotations.NEGATIVE_HALF_PI,
        Rotations.NEGATIVE_HALF_PI: Rotations.ZERO
    },
    Rotations.PI: {
        Rotations.ZERO: Rotations.PI,
        Rotations.HALF_PI: Rotations.NEGATIVE_HALF_PI,
        Rotations.PI: Rotations.ZERO,
        Rotations.NEGATIVE_HALF_PI: Rotations.HALF_PI
    },
    Rotations.NEGATIVE_HALF_PI: {
        Rotations.ZERO: Rotations.NEGATIVE_HALF_PI,
        Rotations.HALF_PI: Rotations.ZERO,
        Rotations.PI: Rotations.HALF_PI,
        Rotations.NEGATIVE_HALF_PI: Rotations.PI
    }
}