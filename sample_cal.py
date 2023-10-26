from model.game_level_2d import GameLevel2D
from model.game_trace_2d import GameOperation
from diversity.average import average_of_difference,average_of_value
from diversity.accumulate_diversity import accumulate_by_coefficients

import logging
logger= logging.getLogger(__name__)


sample_level1=GameLevel2D(list([list([1,2,3]),list([2,3,4])]))
sample_level2=GameLevel2D(list([list([1,2,3]),list([2,3,6])]))
sample_level3=GameLevel2D(list([list([1,2,3]),list([2,3,4])]))

level_set1=[sample_level1,sample_level2]
level_set2=[sample_level1,sample_level3]
level_set3=[sample_level1,sample_level2,sample_level3]

print(average_of_difference(GameLevel2D.calculate_different_elements)(level_set1))
print(average_of_difference(GameLevel2D.calculate_different_elements)(level_set2))
print(average_of_difference(GameLevel2D.calculate_different_elements)(level_set3))

try:
    GameLevel2D.calculate_leniency(sample_level1,{1:1,2:2,3:3},allow_undefined=False)
except Exception as e:
    logger.warning(f"e:{e}")
    
dict= {1:1,2:2,3:3}
    
print(GameLevel2D.calculate_leniency(sample_level1,{1:1,2:2,3:3}))
    
print(GameLevel2D.calculate_leniency(sample_level1,{1:1,2:2,3:3,4:4},allow_undefined=False))


print(average_of_value(GameLevel2D.calculate_leniency,dict)(level_set1))


average_value=average_of_value(GameLevel2D.calculate_leniency,dict)(level_set1)
average_difference= average_of_difference(GameLevel2D.calculate_different_elements)(level_set1)

functions = [(average_of_value(GameLevel2D.calculate_leniency,dict),1),
                       (average_of_difference(GameLevel2D.calculate_different_elements),2)]

print(f"accumulate result:{accumulate_by_coefficients(functions=functions,objects=level_set1)}")
print(f"real result:{average_of_value(GameLevel2D.calculate_leniency,dict)(level_set1)+average_of_difference(GameLevel2D.calculate_different_elements)(level_set1)*2}")


trace1 = GameOperation([(0,1),(1,2),(2,3)])
trace2 = GameOperation([(0,1),(2,3),(1,2)])
trace3 = GameOperation([(0,1),(1,3),(2,2)])
trace4 = GameOperation([(0,1),(1,3),(2,2),(3,3)])
trace5 = GameOperation([(0,0),(1,0),(2,0),(3,0),(4,0)])

print(GameOperation.calculate_minimum_edit_distance(trace1,trace2))
print(GameOperation.calculate_minimum_edit_distance(trace1,trace3))
print(GameOperation.calculate_minimum_edit_distance(trace1,trace4))
print(GameOperation.calculate_minimum_edit_distance(trace1,trace5))

trace_set1=[trace1,trace2,trace3,trace4,trace5]
print(average_of_difference(GameOperation.calculate_minimum_edit_distance)(trace_set1))