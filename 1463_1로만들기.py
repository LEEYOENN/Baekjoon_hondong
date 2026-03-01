import sys
input = sys.stdin.readline

n = int(input())

# DP 테이블 초기화 (0부터 n까지)
# dp[i]는 i를 1로 만드는데 필요한 최소 연산 횟수
dp = [0] * (n + 1)

# 2부터 n까지 바텀업(Bottom-up) 방식으로 계산
for i in range(2, n + 1):
    # 1. 1을 빼는 경우 (기본 전제)
    dp[i] = dp[i-1] + 1
    
    # 2. 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        # 1을 뺀 경우와 2로 나눈 경우 중 더 작은 값 선택
        dp[i] = min(dp[i], dp[i//2] + 1)
        
    # 3. 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        # 현재 값(1을 뺐거나 2로 나눈 최솟값)과 3으로 나눈 경우 중 더 작은 값 선택
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])