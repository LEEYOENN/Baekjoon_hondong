import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

# dp 테이블 초기화, 각 숫자는 최소 자기자신만이므로 모두 1로 초기화
dp = [1] * n

# 현재 확인하는 숫자 인덱스 i
for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            

print(max(dp))