import math
import random
from copy import deepcopy
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
        total_probabilities = []
        for block_type, rotations in self.possible_blocks.items():
            weight_data = block_type.value
            total_weight = weight_data["total_weight"]
            print("total_weight for", block_type.name, ":", total_weight)

            # Collect probabilities for all subtypes
            for subtype, weight in weight_data.items():
                print(f"Processing {block_type.name} subtype {subtype} with weight {weight}")
                if subtype == "total_weight":
                    continue
                prob = weight / total_weight if total_weight > 0 else 0
                print(f"Probability for {block_type.name} subtype {subtype}: {prob}")
                if prob > 0:
                    total_probabilities.append(prob)
                    print(prob)

        # Compute entropy
        self.entropy = -sum(p * math.log2(p) for p in total_probabilities if p > 0)
        print(self.entropy)

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