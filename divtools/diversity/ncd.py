import numpy as np
import zlib
import gzip
from divtools.model.game_level_2d import GameLevel2D

def compress(data):
    """使用zlib、gzip压缩数据."""
    return gzip.compress(data)


def ncd(level1: GameLevel2D, level2: GameLevel2D):
    l1 = np.asarray(level1.map, dtype=np.int32)
    l2 = np.asarray(level2.map, dtype=np.int32)

    serialize1 = l1.tobytes()
    serialize2 = l2.tobytes()

    c_x = len(compress(serialize1))
    c_y = len(compress(serialize2))
    c_xy = len(compress(serialize1 + serialize2))

    return (c_xy - min(c_x, c_y)) / max(c_x, c_y)

