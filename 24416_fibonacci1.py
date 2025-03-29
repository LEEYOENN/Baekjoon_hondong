import sys
n = int(sys.stdin.readline())
n1, n2 = 0, 0

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fibbonacci(n):
    f = [0] * (n + 1)
    f[1], f[2] = 1, 1
    for i in range(3, n + 1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

fib(n)
fibbonacci(n)

print(fib(n), end=" ")
print(n-2)
