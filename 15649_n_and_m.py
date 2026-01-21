import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [] # 방문한 숫자를 담을 스택(리스트)

def dfs():
    # 목표한 길이 m에 도달하면 출력
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        # 중복 방지: 이미 s에 있는 숫자는 건너뜀
        if i not in s:
            s.append(i) # 방문 처리
            dfs()       # 다음 깊이로 이동
            s.pop()     # 방문 완료 후 상태 원상복구 (백트래킹 핵심)

dfs()