import pprint
from copy import deepcopy

from enums import Directions
from world.consts.Others import DIRECTION_MAP, ROTATION_ADD
from world.consts.Rules import *

class WorldBlock:
    def __init__(self, rotation: Rotations, coord: tuple[int, int, int], world_block_type: WorldBlockTypes, subtype:str):
        self.rotation = rotation
        self.coord = coord
        self.world_block_type = world_block_type
        self.subtype = subtype

    def get_building_rules(self, direction: Directions):
        """Returns neighbor rules for given world direction, accounting for rotation"""
        # Handle top/bottom immediately
        if direction in (Directions.TOP, Directions.BOTTOM):
            return None

        # Get original direction relative to unrotated block
        original_dir = DIRECTION_MAP[self.rotation].get(direction)
        if original_dir is None:
            return None

        # Get base rules for this block type and original direction
        base_rules = world_rules.get(self.world_block_type, {}).get(original_dir)
        if base_rules is None:
            return None

        # Adjust neighbor rotations for current block's rotation
        adjusted_rules = {}
        for neighbor_type, rotations in base_rules.items():
            adjusted_rots = []
            for rot in rotations:
                abs_rot = ROTATION_ADD[self.rotation].get(rot)
                if abs_rot is not None:
                    adjusted_rots.append(abs_rot)
            adjusted_rules[neighbor_type] = adjusted_rots

        return adjusted_rules




    def __repr__(self):
        # return f"WorldBlock(coord={self.coord}, type={self.world_block_type.name}, subtype={self.subtype}, rotation={self.rotation.name})"
        return f"modelFromData( ModelTypes.{self.subtype}, Rotations.{self.rotation.name}, new Vector3({self.coord[0] *2}, {self.coord[1]*2}, {self.coord[2]*2}))"