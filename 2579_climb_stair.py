import sys
input = sys.stdin.readline

n = int(input())
s = [ int(input()) for _ in range(n) ]
dp = [0] * n

# 계단이 2칸 이하면 그냥 합 출력력
if n <= 2:
    print(sum(s))
else:
    # 먼저 3칸까지는 일반 대입문으로 넣는다다
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    dp[2] = max(s[0] + s[2], s[1] + s[2])
    # 세번째 칸부터는 점화식 사용용
    for i in range(3, n):
        #바로밑에서 올라오는 경우와 두칸 밑에서 올라오는 경우 둘중에 max를 dp에 저장장
        dp[i] = max(dp[i-2] + s[i], dp[i-3] + s[i-1] + s[i])

    print(dp[n-1])