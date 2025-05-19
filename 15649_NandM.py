# 백트랙킹은 모든 가능한 경우의 수를 탐색하면서, 조건에 맞지 않는 경우에는 탐색을 중단하고 도돌아가는 기법
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * (n+1)
rslt = []

def backTrack():
    if len(rslt) == m:
        print(*rslt)
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True #숫자 i를 사용했다고 표시
            rslt.append(i) #i를 rslt에 삽입
            backTrack() #다음 숫자 다시고르라고 재귀 호출
            visited[i] = False # 백트랙킹: i의 사용을 취소
            rslt.pop() # 백트랙킹: i를 제거

backTrack()