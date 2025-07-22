import sys
import heapq

input = sys.stdin.readline
N = int(input())

heap = []

for _ in range(N):
    x = int(input())
    
    if x != 0:
        # (절댓값, 실제값)을 힙에 넣음
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            # 우선순위에 따라 출력
            print(heapq.heappop(heap)[1])
        else:
            print(0)