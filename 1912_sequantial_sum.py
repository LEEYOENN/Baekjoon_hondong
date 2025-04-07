import sys
n = int(sys.stdin.readline())

seq = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
dp[0] = seq[0]
for i in range(1, n):
    dp[i] = max(dp[i-1] + seq[i], seq[i])

print(max(dp))