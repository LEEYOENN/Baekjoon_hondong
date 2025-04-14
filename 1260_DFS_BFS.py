import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

lines = [ list(map(int, input().split())) for _ in range(m) ]

print(lines)