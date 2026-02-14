import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] * 301 # 계단 점수 (N은 최대 300)
dp = [0] * 301     # dp 테이블

for i in range(1, n + 1):
    stairs[i] = int(input())

# 초기값 설정 (매우 중요)
dp[1] = stairs[1]
if n > 1:
    dp[2] = stairs[1] + stairs[2]

# 점화식:
# 3번째 계단(i)에 도착하는 방법은 딱 두 가지입니다.
# 1. (i-3) -> (i-1) -> (i) : 전전 칸은 건너뛰고, 바로 전 칸을 밟고 온 경우
# 2. (i-2) -> (i)          : 전전 칸을 밟고, 한 번에 두 칸 올라온 경우

for i in range(3, n + 1):
    # 두 경우 중 점수가 더 높은 것을 선택
    # Case 1: dp[i-3] + stairs[i-1] + stairs[i]
    # Case 2: dp[i-2] + stairs[i]
    dp[i] = max(dp[i-3] + stairs[i-1], dp[i-2]) + stairs[i]

print(dp[n])