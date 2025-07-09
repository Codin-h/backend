from enum import Enum
import world.consts.WorldBlockSubType as subType

class WorldBlockTypes(Enum):
    BUILDINGS = subType.BUILDINGS
    ROADS = subType.ROADS
    CORNERS = subType.CORNERS
    JUNCTIONS = subType.JUNCTIONS
    INTERSECTIONS = subType.INTERSECTIONS

    @staticmethod
    def get_probability_for(block_type: 'WorldBlockTypes', subtype_name: str) -> float:
        block_weights = block_type.value
        total_weight = block_weights["total_weight"]
        subtype_weight = block_weights.get(subtype_name, 0.0)
        return subtype_weight / total_weight if total_weight > 0 else 0.0
