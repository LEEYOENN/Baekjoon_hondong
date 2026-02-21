import sys
input = sys.stdin.readline

# n: 수의 개수, m: 합을 구해야 하는 횟수
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 누적 합(Prefix Sum)을 저장할 배열 초기화
# 계산의 편의를 위해 맨 앞에 0을 패딩해 줌 (크기가 n+1)
prefix_sum = [0] * (n + 1)

# 누적 합 계산: prefix_sum[k]는 1번째부터 k번째까지의 합
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + data[i]

# M개의 구간에 대해 합 구하기
for _ in range(m):
    i, j = map(int, input().split())
    
    # j번째까지의 누적 합에서 (i-1)번째까지의 누적 합을 빼면
    # 정확히 i번째부터 j번째까지의 합만 남게 됨 (O(1) 시간 복잡도)
    print(prefix_sum[j] - prefix_sum[i-1])