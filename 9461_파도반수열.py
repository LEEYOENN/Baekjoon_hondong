import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    
    n = int(input())
    
    if n == 1 or n == 2 or n == 3:
        print(1)
        continue

    dp = [0] * (n+1)
    
    dp[1], dp[2], dp[3] = 1,1,1
    
    for i in range(4, n+1):
        dp[i] = dp[i - 2] + dp[i - 3]
        
    print(dp[n])