import sys
input = sys.stdin.readline

# n: 수열의 길이, m: 찾고자 하는 부분합
n, m = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    # interval_sum이 m보다 작고, end가 범위를 벗어나지 않을 때까지
    while interval_sum < m and end < n:
        interval_sum += nums[end]
        end += 1
    
    # 부분합이 m과 같다면 카운트 증가
    if interval_sum == m:
        count += 1
    
    # 다음 loop에서 start가 1 증가하므로, 현재 start 값은 부분합에서 제외
    interval_sum -= nums[start]

print(count)