
from common.model import Model
from typing import List


class GameLevel2D(Model):
    rows: int
    columns: int
    map: List[List[int]]
    
    def __init__(self,map:List[List[int]]):
        self.map=map
        self.rows=len(map)
        self.columns=len(map[0])
        
    