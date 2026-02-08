import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
queue = deque()

# 맵 정보를 입력받으면서, 동시에 익은 토마토(1)의 위치를 큐에 모두 넣음
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 내에 있고, 안 익은 토마토(0)라면
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                # 익게 만들고(1 더하기), 큐에 추가
                # 여기서 graph[x][y] + 1은 "걸린 일수"를 의미함
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

bfs()

result = 0
for i in graph:
    for j in i:
        # 다 돌았는데도 안 익은 토마토(0)가 남아있다면 실패
        if j == 0:
            print(-1)
            exit()
        # 가장 오래 걸린 날짜 찾기
        result = max(result, j)

# 시작할 때 1로 시작했으므로 결과에서 1을 빼줌
print(result - 1)