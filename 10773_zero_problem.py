import sys

k = int(sys.stdin.readline().strip())

stack = []

for _ in range(k):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        stack.pop()
    else:
        stack.append(x)

print(sum(stack))