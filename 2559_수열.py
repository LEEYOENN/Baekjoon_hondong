import sys
input = sys.stdin.readline

n, k = map(int, input().split())

temp = list(map(int, input().split()))

# 슬라이딩 윈도우 아이디어
# 예를 들어 K=3일 때:

# 첫 합: temp[0] + temp[1] + temp[2]
# 다음 합: 이전 합 - temp[0] + temp[3]

# → 즉, 이전 구간에서 빠진 값은 빼고, 새로 들어온 값은 더한다.

#첫번째 구간 합 초기화
window_sum = sum(temp[:k])
max_sum = window_sum

for i in range(k, n):
    window_sum = window_sum - temp[i - k] + temp[i]
    max_sum = max(max_sum, window_sum)

print(max_sum)











# hap = [0] * (n - k + 1)

# for i in range(n - k + 1):
#     for j in range(i, i + k):
#         hap[i] += temp[j]
        
# print(max(hap))

#시간초과 슬라이딩 윈도우 사용
#O(N*k) -> O(N) 으로 줄일 수있음음