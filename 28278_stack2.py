import sys

n = int(sys.stdin.readline().strip())
stack = []

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == '1':
        x = int(command[1])
        stack.append(x)
    elif command[0] == '2':
        if len(stack) != 0:
            print(stack.pop())
        else: print(-1)
    elif command[0] == '3':
        print(len(stack))
    elif command[0] == '4':
        if len(stack) == 0:
            print(1)
        else: print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else: print(stack[len(stack) -1])