import sys
input = sys.stdin.readline
n = int(input())
amount = [0]
[ amount.append(int(input())) for _ in range(n)]

if n == 1:
    print(amount[1])
elif n == 2:
    print(amount[1] + amount[2])
else: 
    dp = [0] * (n + 1)
    dp[1] = amount[1]
    dp[2] = amount[1] + amount[2]
    dp[3] = max(dp[2], amount[1]+amount[3], amount[2]+ amount[3])
    
    for i in range(4, n+1):
        dp[i] = max(dp[i - 2] + amount[i], 
                    dp[i - 3] + amount[i - 1] + amount[i], 
                    dp[i - 1])

    print(dp[n])
    
##현재 i번째를 포함 안하고 넘어가는게 제일 클 수 있다는 걸 고려 못해서 틀렸었음