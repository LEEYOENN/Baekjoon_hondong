# 백준 7785번 - "회사에 있는 사람" -집합
import sys

input = sys.stdin.readline

n = int(input()) 
data = set() #set은 중복을 허용하지 않고, 빠르게 추가/삭제/탐색 가능

for i in range (n):
    name, behave = input().split()
    if behave == 'enter':
        data.add(name)
    elif behave == 'leave':
        data.discard(name) #discard()는 없으면 조용히 넘어감, remove()는 에러 발생시킴
data = sorted(data, reverse=True)

for name in data:
    print(name)