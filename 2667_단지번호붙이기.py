import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0  # 방문 처리 (1을 0으로 바꿔서 다시 방문 안 하게 함)
    count = 1        # 현재 단지의 집 개수
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 지도 범위 내에 있고, 집이 있는 곳(1)이라면
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0  # 방문 처리
                q.append((nx, ny))
                count += 1
                
    return count

complex_counts = [] # 각 단지의 집 개수를 담을 리스트

# 지도 전체를 돌면서 1(집)을 만나면 BFS 시작
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            # BFS가 끝나면 그 단지의 집 개수를 리스트에 추가
            complex_counts.append(bfs(i, j))

# 결과 출력
complex_counts.sort() # 오름차순 정렬 조건
print(len(complex_counts)) # 총 단지 수
for count in complex_counts:
    print(count)