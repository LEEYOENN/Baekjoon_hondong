import sys
input = sys.stdin.readline

n, m = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(n)]

# 2차원 누적합 배열
prefix = [ [0] * n for _ in range(n)]
prefix[0][0] = table[0][0]

#prefix의 첫행과 첫열을 채우기기
for i in range(1, n):
    prefix[0][i] = prefix[0][i-1] + table[0][i]
for i in range(1, n):
    prefix[i][0] = prefix[i-1][0] + table[i][0]

#prefix의 나머지 부분 채우기
for i in range(1, n):
    for j in range(1, n):
        # prefix[i-1][j]: (i,j) 위쪽 전체 합
        # prefix[i][j-1]: (i,j) 왼쪽 전체 합
        # 근데 두 개를 더하면 (i-1, j-1) 부분이 두 번 더해짐 → 한 번 빼줌
        prefix[i][j] = table[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

#2D Prefix
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
        # 1-based → 0-based 변환
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    
    #전체 누적합에서 가장 큰 사각형 (0,0) ~ (x2,y2)까지의 전체 합을 먼저 가져옵니다.
    total = prefix[x2][y2]
    if x1 > 0:
        # 위쪽 잘라냄
        # → (0,0)~(x1-1,y2) 사각형을 뺍니다.
        # → 위에서 구하고자 하는 구간 위쪽 부분을 제거합니다.
        total = total - prefix[x1-1][y2]
    if y1 > 0:
        # 왼쪽 잘라냄
        # → (0,0)~(x2,y1-1) 사각형을 뺍니다.
        # → 구간 왼쪽 부분 제거합니다.
        total = total - prefix[x2][y1-1]
    if x1 > 0 and y1 > 0:
        # 중복 제거
        # → 위에서 두 번 뺀 부분인 (0,0)~(x1-1,y1-1) 사각형을 한 번 더해줍니다.
        # → 두 번 뺀 것을 한 번 다시 더해줌 = Inclusion-Exclusion 원리!
        total += prefix[x1-1][y1-1]

    print(total)
    