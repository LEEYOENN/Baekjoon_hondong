import sys
from collections import deque
n = int(sys.stdin.readline())

q = deque()
for i in range(1, n+1):
    q.append(i)
    
while len(q) != 1:
    q.popleft()
    temp = q.popleft()
    q.append(temp)
    
print(q[0])