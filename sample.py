from model.game_level_2d import GameLevel2D
from diversity.average_diversity import average_diversity
import numpy as np
from graph.hexbin_graph import draw_hexbin

import logging
logger= logging.getLogger(__name__)


sample_level1=GameLevel2D(list([list([1,2,3]),list([2,3,4])]))
sample_level2=GameLevel2D(list([list([1,2,3]),list([2,3,6])]))
sample_level3=GameLevel2D(list([list([1,2,3]),list([2,3,4])]))

level_set1=set({sample_level1,sample_level2})
level_set2=set({sample_level1,sample_level3})
level_set3=set({sample_level1,sample_level2,sample_level3})

print(average_diversity(GameLevel2D.calculate_different_elements)(level_set1))
print(average_diversity(GameLevel2D.calculate_different_elements)(level_set2))
print(average_diversity(GameLevel2D.calculate_different_elements)(level_set3))



x = "x"
y = 'y'

data = np.random.random((2000, 2))
data = data.tolist()
draw_hexbin(x, y, data)


try:
    GameLevel2D.calculate_leniency(sample_level1,{1:1,2:2,3:3},allow_undefined=False)
except Exception as e:
    logger.warning(f"e:{e}")
    
    
print(GameLevel2D.calculate_leniency(sample_level1,{1:1,2:2,3:3}))
    
print(GameLevel2D.calculate_leniency(sample_level1,{1:1,2:2,3:3,4:4},allow_undefined=False))
    
    