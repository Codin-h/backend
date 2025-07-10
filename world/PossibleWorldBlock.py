import math
import random
from copy import deepcopy
from pprint import pprint

from world.consts.Others import *


class PossibleWorldBlock:
    def __init__(self):
        self.possible_blocks = deepcopy(possible_blocks)
        self._compute_entropy()

    def update(self, rules: dict):

        for world_block_type, rotations in rules.items():
            if world_block_type in self.possible_blocks:
                self.possible_blocks[world_block_type] = [
                    rotation for rotation in self.possible_blocks[world_block_type]
                    if rotation not in rotations
                ]
        self._compute_entropy()

    def _compute_entropy(self):

        total_global_weight = 0.0
        # First pass: compute total weight of all possible tiles (subtypes * rotations)
        for block_type, rotations in self.possible_blocks.items():
            weight_data = block_type.value
            for subtype, weight_val in weight_data.items():
                if subtype == "total_weight":
                    continue
                # Multiply subtype weight by number of rotations
                total_global_weight += weight_val * len(rotations)

        # Handle case with no possible tiles
        if total_global_weight <= 0:
            self.entropy = 0
            return

        entropy = 0.0
        # Second pass: compute entropy contributions
        for block_type, rotations in self.possible_blocks.items():
            weight_data = block_type.value
            for subtype, weight_val in weight_data.items():
                if subtype == "total_weight" or weight_val <= 0:
                    continue

                count = len(rotations)  # Number of rotations for this block
                p = (weight_val * count) / total_global_weight  # Global probability

                if p > 0:
                    entropy -= p * math.log2(p)  # Entropy contribution

        self.entropy = entropy

    def get_entropy(self) -> float:
        return self.entropy


    def collapse(self):
        """
        Collapses the possible world block into a single subtype and rotation.
        Returns a tuple: (WorldBlockType, subtype_name, rotation)
        """
        # Filter out types with no possible rotations
        valid_types = [t for t, r in self.possible_blocks.items() if r]

        if not valid_types:
            raise ValueError("No valid WorldBlockTypes left to collapse.")

        # Pick one WorldBlockType randomly
        block_type = random.choice(valid_types)

        # Get subtype and weights
        weight_data =  block_type.value
        subtypes = [k for k in weight_data.keys() if k != "total_weight"]
        weights = [weight_data[k] for k in subtypes]

        # Weighted random choice of subtype
        chosen_subtype = random.choices(subtypes, weights=weights, k=1)[0]

        # Randomly select one of the available rotations
        rotation = random.choice(self.possible_blocks[block_type])

        return block_type, chosen_subtype, rotation

    def __repr__(self):
        return f"PossibleWorldBlock(possible_blocks={self.possible_blocks}, entropy={self.entropy})"