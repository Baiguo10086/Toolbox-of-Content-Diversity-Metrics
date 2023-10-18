
from common.model import Model
from typing import List,Dict


class GameLevel2D(Model):
    rows: int
    columns: int
    map: List[List[int]]
    def __init__(self,map:List[List[int]]):
        self.map=map
        self.rows=len(map)
        self.columns=len(map[0])
    
    @classmethod
    def calculate_different_elements(cls, obj1, obj2) -> int:
        if not isinstance(obj1,cls) or not isinstance(obj2,cls):
            raise ValueError(f"object is not class of {cls.__name__}")
        
        if (obj1.rows,obj1.columns)!=(obj2.rows,obj2.columns):
            raise ValueError(f"size of game level not match")
        
        count = 0
        for x in range(obj1.rows):
            for y in range(obj1.columns):
                if obj1.map[x][y] != obj2.map[x][y]:
                    count+=1

        return count

    @classmethod
    def calculate_leniency(cls,obj,value_dict:Dict[int,float],allow_undefined:bool =True) -> float:
        if not isinstance(obj,cls):
            raise ValueError(f"object is not class of {cls.__name__}")
        
        result = 0 
        for x in range(obj.rows):
            for y in range(obj.columns):
                if (not allow_undefined) and (value_dict.get(obj.map[x][y]) is None):
                    raise ValueError(f"object contain undefined value : {obj.map[x][y]}")
                result+=value_dict.get(obj.map[x][y],0)
        
        return result