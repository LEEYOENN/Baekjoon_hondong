import sys
n = int(sys.stdin.readline())

cost = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]

dp = [[0]*3 for _ in range(n)]

#첫번째 집은 그대로
dp[0][0] = cost[0][0]  # R
dp[0][1] = cost[0][1]  # G
dp[0][2] = cost[0][2]  # B

for i in range(1, n):
    dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])
    
print(min(dp[n-1]))
