import numpy as np
from divtools.model.game_level_2d import GameLevel2D
from typing import List


def horizontal_symmetry(segment: GameLevel2D):
    # Convert segment to a NumPy array for vectorization
    if len(segment.map) % 2 == 1:
        raise ValueError(f"width needs to be an even number")
    segment = np.array(segment.map)

    # Calculate the symmetry score using vectorized comparison
    symmetry = np.sum(segment[:int(len(segment) / 2)] == segment[len(segment) - 1::-1][:int (len(segment) / 2)])

    return symmetry


def vertical_symmetry(segment: GameLevel2D):
    # Convert segment to a NumPy array for efficient operations
    if len(segment.map[0]) % 2 == 1:
        raise ValueError(f"width needs to be an even number")
    left_half = np.array([row[:int(len(segment.map[0])/2)] for row in segment.map])
    right_half = np.array([row[int(len(segment.map[0])/2):] for row in segment.map])
    right_half[:, :] = right_half[:, ::-1]
    # print(left_half)
    # print(right_half)
    # Calculate the symmetry score using vectorized comparison
    symmetry = np.sum(left_half == right_half)

    return symmetry


def total_symmetry(segment: GameLevel2D):
    return horizontal_symmetry(segment) + vertical_symmetry(segment)
