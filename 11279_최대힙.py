import sys
import heapq
input = sys.stdin.readline()
n = int(input())

max_heap = []

for _ in range(n):
    x = int(input())
    if x > 0 :
        #최대힙으로 사용하려면 음수로 push 해야함
        heapq.heappush(max_heap, -x)
        
    else :
        if max_heap:
            #음수로 넣었기 때문에 다시 마이너스 붙이기
            print(-(heapq.heappop(max_heap)))
        else:
            print(0)