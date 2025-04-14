from collections import deque
import sys
input = sys.stdin.readline

deq = deque()
n = int(input())

for i in range(n):
    cmd = input().split()
    
    if cmd[0] == '1':
        deq.appendleft(int(cmd[1]))
    elif cmd[0] == '2':
        deq.append(int(cmd[1]))
    elif cmd[0] == '3':
        if deq: print(deq.popleft())
        else: print(-1)
    elif cmd[0] == '4':
        if deq: print(deq.pop())
        else: print(-1)
    elif cmd[0] == '5':
        print(len(deq))
    elif cmd[0] == '6':
        if deq: print(0)
        else: print(1)
    elif cmd[0] == '7':
        if deq: print(deq[0])
        else: print(-1)
    elif cmd[0] == '8':
        if deq: print(deq[-1])
        else: print(-1)