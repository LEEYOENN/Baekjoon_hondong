import sys
input = sys.stdin.readline

n = int(input())

# dp 테이블 초기화 (n은 최대 1000)
dp = [0] * 1001

# 초기값 설정
# 2x1 직사각형을 채우는 방법: 1가지 (세로 1개)
dp[1] = 1
# 2x2 직사각형을 채우는 방법: 2가지 (세로 2개, 가로 2개)
dp[2] = 2

# 점화식: dp[i] = dp[i-1] + dp[i-2]
# 마지막에 타일 하나를 세로로 놓는 경우(dp[i-1])와 
# 가로로 두 개 놓는 경우(dp[i-2])의 합
for i in range(3, n + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])