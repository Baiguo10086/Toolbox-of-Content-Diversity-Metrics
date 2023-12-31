
from divtools.common.model import Model
from typing import List,Tuple,Optional

class GameOperationSequence(Model):
    operations: List[Tuple[float,int]]
    def __init__(self,operations:List[Tuple[float,int]]):
        self.operations=sorted(operations)
class Position():
    pass

class Position2D(Position):
    x: float
    y: float
    def __init__(self,position) -> None:
        self.x = position[0]
        self.y = position[1]
    
    
class GameTrace(Model):
    position_type: type
    positions: List[Position]
    
    def __init__(self,position_type,positions:Optional[List]=[]):
        if not issubclass(position_type, Position):
            raise ValueError("Invalid type. It should be a subclass of Position.")
        self.position_type = position_type
        self.positions = []
        for position in positions:
            self.positions.append(position_type(position))



class GameTraceWithTime(Model):
    position_type: type
    positions: List[Tuple[float,Position]]
    
    def __init__(self,position_type,positions:Optional[List[Tuple]]=[]):
        if not issubclass(position_type, Position):
            raise ValueError("Invalid type. It should be a subclass of Position.")
        self.position_type = position_type
        self.positions = []
        for position in positions:
            self.positions.append((position[0],position_type(position[1])))

        self.positions=sorted(self.positions)