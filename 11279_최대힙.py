import sys
import heapq
input = sys.stdin.readline
n = int(input())

max_heap = []

#최대힙으로 사용하려면 음수로 push 해야함
for _ in range(n):
    x = int(input())
    if x > 0 :
        heapq.heappush(max_heap, -x)
        
    else :
        if max_heap:
            #음수로 넣었기 때문에 다시 마이너스 붙여애됨
            print(-(heapq.heappop(max_heap)))
        else:
            print(0)