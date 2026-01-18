import sys
from collections import deque

# 입력 속도를 높이기 위한 설정
input = sys.stdin.readline

def dfs(idx):
    # 방문 처리
    visited_dfs[idx] = True
    print(idx, end=' ')
    
    # 연결된 노드 방문
    for i in range(1, n + 1):
        if not visited_dfs[i] and graph[idx][i]:
            dfs(i)

def bfs(idx):
    q = deque([idx])
    visited_bfs[idx] = True
    
    while q:
        current = q.popleft()
        print(current, end=' ')
        
        for i in range(1, n + 1):
            if not visited_bfs[i] and graph[current][i]:
                q.append(i)
                visited_bfs[i] = True

# N: 정점 개수, M: 간선 개수, V: 시작 정점
n, m, v = map(int, input().split())

# 인접 행렬 생성 (번호가 1부터 시작하므로 n+1 크기)
graph = [[False] * (n + 1) for _ in range(n + 1)]
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

# 간선 연결
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# 실행
dfs(v)
print() # 줄바꿈
bfs(v)