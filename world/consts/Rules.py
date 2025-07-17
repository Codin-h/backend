from enums.Directions import Directions
from enums.Rotations import Rotations
from enums.WorldBlockTypes import WorldBlockTypes

"""
    foreach type there is a number of rules for each direction and each type of block
"""
world_rules = {
    WorldBlockTypes.BUILDINGS : {
        Directions.SOUTH: {
            WorldBlockTypes.BUILDINGS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.ROADS: [Rotations.ZERO, Rotations.PI],
            WorldBlockTypes.CORNERS: [ Rotations.HALF_PI, Rotations.PI],
            WorldBlockTypes.JUNCTIONS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.INTERSECTIONS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI],
        },
        Directions.NORTH: {
            WorldBlockTypes.BUILDINGS: [Rotations.ZERO],
            WorldBlockTypes.ROADS: [Rotations.ZERO, Rotations.PI],
            WorldBlockTypes.CORNERS: [ Rotations.NEGATIVE_HALF_PI, Rotations.ZERO],
            WorldBlockTypes.JUNCTIONS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.INTERSECTIONS: [Rotations.ZERO, Rotations.NEGATIVE_HALF_PI, Rotations.PI],
        },
        Directions.WEST: {
            WorldBlockTypes.BUILDINGS: [Rotations.HALF_PI],
            WorldBlockTypes.ROADS: [Rotations.NEGATIVE_HALF_PI, Rotations.HALF_PI],
            WorldBlockTypes.CORNERS: [ Rotations.ZERO, Rotations.HALF_PI],
            WorldBlockTypes.JUNCTIONS: [Rotations.NEGATIVE_HALF_PI, Rotations.ZERO, Rotations.HALF_PI, Rotations.PI],
            WorldBlockTypes.INTERSECTIONS: [Rotations.NEGATIVE_HALF_PI, Rotations.ZERO, Rotations.HALF_PI],
        },
        Directions.EAST: {
            WorldBlockTypes.BUILDINGS: [Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.ROADS: [Rotations.NEGATIVE_HALF_PI, Rotations.HALF_PI],
            WorldBlockTypes.CORNERS: [ Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.JUNCTIONS: [Rotations.NEGATIVE_HALF_PI, Rotations.ZERO, Rotations.HALF_PI, Rotations.PI],
            WorldBlockTypes.INTERSECTIONS: [Rotations.NEGATIVE_HALF_PI, Rotations.PI, Rotations.HALF_PI],
        },
        Directions.TOP: None,
        Directions.BOTTOM: None
    },

    WorldBlockTypes.ROADS : {
        Directions.SOUTH: {
            WorldBlockTypes.BUILDINGS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.ROADS: [Rotations.HALF_PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.CORNERS: [ Rotations.ZERO, Rotations.NEGATIVE_HALF_PI ],
            WorldBlockTypes.JUNCTIONS: [],
            WorldBlockTypes.INTERSECTIONS: [Rotations.NEGATIVE_HALF_PI],
        },
        Directions.NORTH: {
            WorldBlockTypes.BUILDINGS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.ROADS: [Rotations.HALF_PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.CORNERS: [ Rotations.HALF_PI, Rotations.PI ],
            WorldBlockTypes.JUNCTIONS: [],
            WorldBlockTypes.INTERSECTIONS: [Rotations.HALF_PI],
        },
        Directions.WEST: {
            WorldBlockTypes.BUILDINGS: [],
            WorldBlockTypes.ROADS: [Rotations.HALF_PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.CORNERS: [ Rotations.ZERO, Rotations.HALF_PI ],
            WorldBlockTypes.JUNCTIONS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.INTERSECTIONS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.NEGATIVE_HALF_PI],
        },
        Directions.EAST: {
            WorldBlockTypes.BUILDINGS: [],
            WorldBlockTypes.ROADS: [Rotations.HALF_PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.CORNERS: [ Rotations.PI, Rotations.NEGATIVE_HALF_PI ],
            WorldBlockTypes.JUNCTIONS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.INTERSECTIONS: [Rotations.NEGATIVE_HALF_PI, Rotations.HALF_PI, Rotations.PI],
        },
        Directions.TOP: None,
        Directions.BOTTOM: None
    },

    WorldBlockTypes.CORNERS : {
        Directions.SOUTH: {
            WorldBlockTypes.BUILDINGS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.ROADS: [Rotations.HALF_PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.CORNERS: [Rotations.ZERO, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.JUNCTIONS: [],
            WorldBlockTypes.INTERSECTIONS: [Rotations.NEGATIVE_HALF_PI],
        },
        Directions.NORTH: {
            WorldBlockTypes.BUILDINGS: [],
            WorldBlockTypes.ROADS: [Rotations.ZERO, Rotations.PI],
            WorldBlockTypes.CORNERS: [Rotations.ZERO, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.JUNCTIONS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.INTERSECTIONS: [Rotations.ZERO, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
        },
        Directions.WEST: {
            WorldBlockTypes.BUILDINGS: [],
            WorldBlockTypes.ROADS: [Rotations.NEGATIVE_HALF_PI, Rotations.HALF_PI],
            WorldBlockTypes.CORNERS: [Rotations.ZERO, Rotations.HALF_PI],
            WorldBlockTypes.JUNCTIONS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.INTERSECTIONS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.NEGATIVE_HALF_PI],
        },
        Directions.EAST: {
            WorldBlockTypes.BUILDINGS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.ROADS: [Rotations.ZERO, Rotations.PI],
            WorldBlockTypes.CORNERS: [Rotations.ZERO, Rotations.HALF_PI],
            WorldBlockTypes.JUNCTIONS: [],
            WorldBlockTypes.INTERSECTIONS: [Rotations.ZERO],
        },
        Directions.TOP: None,
        Directions.BOTTOM: None
    },

    WorldBlockTypes.JUNCTIONS : {
        Directions.SOUTH: {
            WorldBlockTypes.BUILDINGS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.ROADS: [Rotations.HALF_PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.CORNERS: [Rotations.ZERO, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.JUNCTIONS: [],
            WorldBlockTypes.INTERSECTIONS: [Rotations.NEGATIVE_HALF_PI],
        },
        Directions.NORTH: {
            WorldBlockTypes.BUILDINGS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.ROADS: [Rotations.HALF_PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.CORNERS: [Rotations.PI, Rotations.HALF_PI],
            WorldBlockTypes.JUNCTIONS: [],
            WorldBlockTypes.INTERSECTIONS: [Rotations.HALF_PI],
        },
        Directions.WEST: {
            WorldBlockTypes.BUILDINGS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.ROADS: [Rotations.ZERO, Rotations.PI],
            WorldBlockTypes.CORNERS: [Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.JUNCTIONS: [],
            WorldBlockTypes.INTERSECTIONS: [Rotations.PI],
        },
        Directions.EAST: {
            WorldBlockTypes.BUILDINGS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.ROADS: [Rotations.ZERO, Rotations.PI],
            WorldBlockTypes.CORNERS: [Rotations.ZERO, Rotations.HALF_PI],
            WorldBlockTypes.JUNCTIONS: [],
            WorldBlockTypes.INTERSECTIONS: [Rotations.ZERO],
        },
        Directions.TOP: None,
        Directions.BOTTOM: None
    },

    WorldBlockTypes.INTERSECTIONS : {
        Directions.SOUTH: {
            WorldBlockTypes.BUILDINGS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.ROADS: [Rotations.HALF_PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.CORNERS: [Rotations.ZERO, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.JUNCTIONS: [],
            WorldBlockTypes.INTERSECTIONS: [Rotations.NEGATIVE_HALF_PI],
        },
        Directions.NORTH: {
            WorldBlockTypes.BUILDINGS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.ROADS: [Rotations.HALF_PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.CORNERS: [Rotations.PI, Rotations.HALF_PI],
            WorldBlockTypes.JUNCTIONS: [],
            WorldBlockTypes.INTERSECTIONS: [Rotations.HALF_PI],
        },
        Directions.WEST: {
            WorldBlockTypes.BUILDINGS: [],
            WorldBlockTypes.ROADS: [Rotations.HALF_PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.CORNERS: [Rotations.ZERO, Rotations.HALF_PI],
            WorldBlockTypes.JUNCTIONS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.INTERSECTIONS: [Rotations.ZERO, Rotations.NEGATIVE_HALF_PI, Rotations.HALF_PI],
        },
        Directions.EAST: {
            WorldBlockTypes.BUILDINGS: [Rotations.ZERO, Rotations.HALF_PI, Rotations.PI, Rotations.NEGATIVE_HALF_PI],
            WorldBlockTypes.ROADS: [Rotations.ZERO, Rotations.PI],
            WorldBlockTypes.CORNERS: [Rotations.ZERO, Rotations.HALF_PI],
            WorldBlockTypes.JUNCTIONS: [],
            WorldBlockTypes.INTERSECTIONS: [Rotations.ZERO],
        },
        Directions.TOP: None,
        Directions.BOTTOM: None
    }
}