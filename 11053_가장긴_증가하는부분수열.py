import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# dp 테이블 초기화: 각 숫자는 최소 자기 자신만으로 길이 1을 가짐
dp = [1] * n

# i: 현재 확인하는 숫자의 인덱스
for i in range(1, n):
    # j: i보다 앞에 있는 숫자들을 확인
    for j in range(i):
        # 내 앞의 숫자(nums[j])가 나(nums[i])보다 작다면 (증가하는 조건)
        if nums[j] < nums[i]:
            # 그 숫자의 dp값 + 1 과 현재 나의 dp값을 비교해 큰 것으로 갱신
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))