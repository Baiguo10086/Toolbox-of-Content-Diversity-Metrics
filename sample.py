from model.GameLevel2D import GameLevel2D
from diversity.average_diversity import average_diversity
import numpy as np
from diversity.hexbinGraph import draw_hexbin



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