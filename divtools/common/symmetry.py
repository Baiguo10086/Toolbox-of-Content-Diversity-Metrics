import numpy as np
from typing import List


def horizontal_symmetry(segment: List):
    # Convert segment to a NumPy array for vectorization
    if len(segment) % 2 == 1:
        raise ValueError(f"width needs to be an even number")
    segment = np.array(segment)

    # Calculate the symmetry score using vectorized comparison
    symmetry = np.sum(segment[:len(segment) / 2] == segment[len(segment) - 1::-1][:len(segment) / 2])

    return symmetry


def vertical_symmetry(segment: List):
    # Convert segment to a NumPy array for efficient operations
    if len(segment[0]) % 2 == 1:
        raise ValueError(f"width needs to be an even number")
    segment = np.array(segment)

    # Select the left and right halves of the array
    left_half = segment[:, :len(segment) / 2]
    right_half = segment[:, len(segment) - 1:len(segment) / 2 - 1:-1]

    # Calculate the symmetry score using vectorized comparison
    symmetry = np.sum(left_half == right_half)

    return symmetry


def total_symmetry(segment):
    return horizontal_symmetry(segment) + vertical_symmetry(segment)
