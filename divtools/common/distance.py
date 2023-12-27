
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


def calculate_constraint_minimum_edit_distance(cls, obj1, obj2, limit:int) -> int:
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
        for y in range(max(0,x-limit),min(m,x+limit)):
            dp[x+1][y+1]=min(dp[x][y+1]+1,dp[x+1][y]+1,dp[x][y]+(0 if obj1.operations[x][1]==obj2.operations[y][1] else 1))
    return dp[n][m]