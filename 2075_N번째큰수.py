import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    numbers = list(map(int, input().split()))
    for num in numbers:
        heapq.heappush(heap, num)
        if len(heap) > n:
            heapq.heappop(heap)  # 가장 작은 값 제거

print(heap[0])  # N번째 큰 수