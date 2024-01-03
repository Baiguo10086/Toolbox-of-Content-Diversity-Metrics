import copy
import numpy as np
from collections import Counter
from divtools.model.game_level_2d import GameLevel2D


def KL_Divergence(p, q):
    p = np.asarray(p, dtype=np.float64)
    q = np.asarray(q, dtype=np.float64)
    q = np.where(q != 0, q, np.finfo(float).eps)

    return np.sum(np.where(p != 0, p * np.log(p / q), 0))


def find_pattern(level: GameLevel2D, eye):
    patterns = Counter()
    level_map = np.asarray(level.map, dtype=np.int32)

    if level_map.shape[0] < eye or level_map.shape[1] < eye:
        return patterns

    for i in range(level_map.shape[0] - (eye - 1)):
        for j in range(level_map.shape[1] - (eye - 1)):
            # Extract the 2x2 sub-array
            sub_array = level_map[i:i + eye, j:j + eye]
            # Convert the sub-array to a tuple and count it
            patterns[tuple(map(tuple, sub_array))] += 1

    return patterns


def KL_Divergence_2d(level1: GameLevel2D, level2: GameLevel2D, eye):
    patterns_original = find_pattern(level1, eye)
    patterns_copy = copy.deepcopy(patterns_original)
    level2_map = np.asarray(level2.map)
    pattern_key = set(patterns_original.keys())
    for p in patterns_copy:
        patterns_copy[p] = 0

    for i in range(level2_map.shape[0] - (eye - 1)):
        for j in range(level2_map.shape[1] - (eye - 1)):
            # Extract the 2x2 sub-array
            sub_array = level2_map[i:i + eye, j:j + eye]
            if tuple(map(tuple, sub_array)) in patterns_copy:
                patterns_copy[tuple(map(tuple, sub_array))] += 1

    values1 = [patterns_original[key] for key in pattern_key]
    values2 = [patterns_copy[key] for key in pattern_key]

    return KL_Divergence(values1, values2)
