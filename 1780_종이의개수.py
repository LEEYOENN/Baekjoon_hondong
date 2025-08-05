import sys
input = sys.stdin.readline()

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

result = [0,0,0]

def check(x, y, n):
    first = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != first:
                return False
    return True

def divide(x, y, n):
    if check(x,y,n):
        result[paper[x][y][+1]] += 1
        return
    
    size = n // 3
    
    for dx in range(3):
        for dy in range(3):
            divide(x + dx*size, y +dy*size, size)
            
# 시작은 (0,0) 부터 전체 크기 N
divide(0,0,n)

#출력
for count in result:
    print(count)
    
    
