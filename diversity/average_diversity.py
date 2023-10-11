
from common.model import Model
from typing import Set

def average_diversity(difference_func):
    def wrapper(obj_set:Set[Model]) -> float:
        found_set:Set = set({})
        if not obj_set:
            raise ValueError("calculate diversity of empty set")
        if len(obj_set)==1:
            raise ValueError("calculate diversity of one object")
            
        difference_sum = 0
        for obj in obj_set:
            for other_obj in found_set:
                difference_sum+=difference_func(obj,other_obj)
            found_set.add(obj)
        
        return difference_sum*2/len(obj_set)/(len(obj_set)-1)
    return wrapper