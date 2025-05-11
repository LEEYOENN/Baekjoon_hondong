import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

#인접리스트 사용
#정점 번호는 1번부터 n번까지 존재
#양방향 그래프이므로 양쪽 모두에 연결
graph = [ [] for _ in range(n+1) ]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
#번호가 작은 점점부터 방문해야해서 정렬렬
for node in graph:
    node.sort()
# DFS 함수 (재귀)

def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)
    
# BFS 함수 (큐)
def bfs(v):
    visited = [False] * (n+1)
    queue = deque([v])
    visited[v] = True
    
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                
#깊이우선탐색 수행
visited = [False] * (n+1)
dfs(v, visited)
print()

#넓이우선탐색 수행
bfs(v)
