import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
balloons = deque(arr)

order = deque([i for i in range(1, n + 1)])
my_order = []
while balloons:
    num = balloons.popleft()
    my_order.append(order.popleft())
    
    if not balloons:
        break
    if num > 0: 
        balloons.rotate(-(num - 1))
        order.rotate(-(num - 1))
    else:
        balloons.rotate(-num)
        order.rotate(-num)
        
print(*my_order)