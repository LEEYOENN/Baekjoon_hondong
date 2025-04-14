import sys
input = sys.stdin.readline
from collections import deque
N, K= map(int, input().split()) ##자료구조 개수

q = deque([ i for i in range(1, N+1) ])
rslt = []

while q:
    q.rotate(1 - K)
    rslt.append(q.popleft())
    
print("<" + ", ".join(map(str, rslt)) +">")

