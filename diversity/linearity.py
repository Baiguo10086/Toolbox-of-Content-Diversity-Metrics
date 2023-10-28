from typing import List
import numpy as np


def linearity(matrix: List[List[int]]):
    m = np.array(matrix)
    col_sum = np.sum(m, axis=0)
    up_mat = np.zeros(m.shape)
    for i in range(len(m) - 1):
        up_mat[i + 1] = up_mat[i] + 1

    col_weight = np.sum(m * up_mat, axis=0) / col_sum
    res = 0
    coe = (col_weight[-1]- col_weight[0])/len(col_weight)
    intercept = col_weight[0]
    for w in range(len(col_weight)):
        res += np.absolute(coe * w + intercept - col_weight[w])

    return res/len(col_weight)
