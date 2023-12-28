from typing import Callable,List

def calculate_minimum_edit_distance(list1:List, list2:List, difference_fn:Callable) -> float:
    
    n=len(list1)
    m=len(list2)
    dp = [[n+m] * (m + 1) for _ in range(n + 1)]
    for x in range(n+1):
        dp[x][0]=x
    for y in range(m+1):
        dp[0][y]=y
    for x in range(n):
        for y in range(m):
            dp[x+1][y]=min(dp[x+1][y],dp[x][y]+1)
            dp[x][y+1]=min(dp[x][y+1],dp[x][y]+1)
            dp[x+1][y+1]=min(dp[x+1][y+1],dp[x][y]+difference_fn(list1[x],list2[y]))
    return dp[n][m]


def calculate_constraint_minimum_edit_distance(list1:List, list2:List, difference_fn:Callable, limit:int) -> float:
    
    n=len(list1)
    m=len(list2)
    dp = [[n+m] * (m + 1) for _ in range(n + 1)]
    for x in range(n+1):
        dp[x][0]=x
    for y in range(m+1):
        dp[0][y]=y
    for x in range(n):
        for y in range(max(0,x-limit),min(m,x+limit)):
            dp[x+1][y]=min(dp[x+1][y],dp[x][y]+1)
            dp[x][y+1]=min(dp[x][y+1],dp[x][y]+1)
            dp[x+1][y+1]=min(dp[x+1][y+1],dp[x][y]+difference_fn(list1[x],list2[y]))
    return dp[n][m]