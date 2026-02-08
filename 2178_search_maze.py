import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

# 미로 맵 입력 받기 (문자열을 리스트로 변환)
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 상하좌우 이동을 위한 방향 벡터 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        # 현재 방향에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우도 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
            # 이전 노드의 거리 + 1을 현재 노드에 저장
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
            
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0, 0))