from enum import Enum
import consts.WorldBlockSubType as subType

class WorldBlockTypes(Enum):
    BUILDINGS = subType.BUILDINGS
    ROADS = subType.ROADS
    CORNERS = subType.CORNERS
    JUNCTIONS = subType.JUNCTIONS
    INTERSECTIONS = subType.INTERSECTIONS

    staticmethod
    def get_total_wheight_for_type(type: 'WorldBlockTypes') -> float:
        """Returns a list of all WorldBlockTypes"""
        if type == WorldBlockTypes.BUILDINGS:
            return sum(subType.BUILDINGS.values())
        elif type == WorldBlockTypes.ROADS:
            return sum(subType.ROADS.values())
        elif type == WorldBlockTypes.CORNERS:
            return sum(subType.CORNERS.values())
        elif type == WorldBlockTypes.JUNCTIONS:
            return sum(subType.JUNCTIONS.values())
        elif type == WorldBlockTypes.INTERSECTIONS:
            return sum(subType.INTERSECTIONS.values())
        else:
            raise ValueError(f"Unknown WorldBlockType: {type}")
        