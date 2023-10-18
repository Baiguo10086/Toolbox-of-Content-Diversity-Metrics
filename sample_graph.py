from model.game_level_2d import GameLevel2D
from diversity.average_diversity import average_diversity_by_difference,average_diversity_by_value
import numpy as np
from graph.hexbin_graph import draw_hexbin

import logging
logger= logging.getLogger(__name__)



x = "x"
y = 'y'

data = np.random.random((2000, 2))
data = data.tolist()
draw_hexbin(x, y, data)

