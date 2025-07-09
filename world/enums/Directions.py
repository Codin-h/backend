from enum import Enum

class Directions(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    TOP = 4
    BOTTOM = 5

    @staticmethod
    def get_direction_from_A_to_B( coordsA: tuple[int, int, int], coordsB: tuple[int, int, int]) -> 'Directions':
        if coordsA[0] < coordsB[0]:
            return Directions.EAST
        elif coordsA[0] > coordsB[0]:
            return Directions.WEST
        elif coordsA[1] < coordsB[1]:
            return Directions.SOUTH
        elif coordsA[1] > coordsB[1]:
            return Directions.NORTH
        elif coordsA[2] < coordsB[2]:
            return Directions.TOP
        elif coordsA[2] > coordsB[2]:
            return Directions.BOTTOM
        else:
            raise ValueError(f"Unable to find the direction from A:{coordsA} to B:{coordsB}")

