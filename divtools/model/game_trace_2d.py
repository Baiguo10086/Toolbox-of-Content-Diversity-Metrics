
from divtools.common.model import Model
from typing import List,Tuple,Optional

class GameOperationSequence(Model):
    operations: List[Tuple[float,int]]
    def __init__(self,operations:List[Tuple[float,int]]):
        self.operations=sorted(operations)
    
    @classmethod
    def calculate_minimum_edit_distance(cls, obj1, obj2) -> int:
        if not isinstance(obj1,cls) or not isinstance(obj2,cls):
            raise ValueError(f"object is not class of {cls.__name__}")
        
        n=len(obj1.operations)
        m=len(obj2.operations)
        dp = [[n+m] * (m + 1) for _ in range(n + 1)]
        for x in range(n+1):
            dp[x][0]=x
        for y in range(m+1):
            dp[0][y]=y
        for x in range(n):
            for y in range(m):
                dp[x+1][y+1]=min(dp[x][y+1]+1,dp[x+1][y]+1,dp[x][y]+(0 if obj1.operations[x][1]==obj2.operations[y][1] else 1))
        return dp[n][m]
    

class Position():
    pass

class Position2D(Position):
    x,y: float
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