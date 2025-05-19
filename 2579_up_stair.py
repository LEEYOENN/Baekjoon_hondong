import sys
n = int(sys.stdin.readline())
stairs = [0]
[ stairs.append(int(sys.stdin.readline())) for _ in range(n)]

if n <= 2:
    print(sum(stairs))
dp = [0] * (n+1)
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + dp[i], dp[i-1])

print(dp[n])