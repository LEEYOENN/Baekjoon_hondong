import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    #모든 수를 다 저장하지 않아도 된다
    nums = list(map(int, input().split()))
    for num in nums:
        heapq.heappush(heap, num)
        
        # 만약 heap의 길이가 n개가 넘으면 가장 작은 수를 pop한다.
        # heap의 길이 n개 유지
        if len(heap) > n:
            heapq.heappop(heap)
# 지금 heap에서 가장 작은 값이 n번째 큰수         
print(heapq.heappop(heap))