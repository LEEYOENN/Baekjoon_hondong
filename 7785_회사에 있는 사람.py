# 백준 7785번 - "회사에 있는 사람"
import sys

input = sys.stdin.readline

n = int(input()) 
data = set()

for i in range (n):
    name, behave = input().split()
    if behave == 'enter':
        data.add(name)
    elif behave == 'leave':
        data.discard(name)
data = sorted(data, reverse=True)
for name in data:
    print(name)