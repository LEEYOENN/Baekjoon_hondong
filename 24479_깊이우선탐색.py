import sys
input = sys.stdin.readline
#최대 정점 수가 100,000개인데, 파이썬 재귀 깊이제한이 1000이라서 풀어줘야한다.
sys.setrecursionlimit(10**6)  
#노드수, 간선수, 시작노드번호
n, m, r = map(int, input().split())

#인접리스트 초기화
graph = [[] for _ in range(n + 1)]

#간선 입력
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
# 각 정점의 방문 순서를 기록
visited = [0] * (n+1)
order = 1

#인접 노드 내림차순 정렬
for i in range(1, n+1):
    graph[i].sort()
    
def dfs(v):
    global order
    visited[v] = order
    for next in graph[v]:
        if visited[next] == 0:
            order += 1
            dfs(next)

dfs(r)

#출력
for i in range(1, n+1):
    print(visited[i])