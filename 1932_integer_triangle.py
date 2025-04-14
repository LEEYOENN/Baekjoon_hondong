import sys
input = sys.stdin.readline

n = int(input())

dp = [[0]*i for i in range(1, n+1) ]
arr = [ list(map(int, input().split())) for _ in range(n)]

# print(arr)
# print(dp)
dp[0][0] = arr[0][0]

# dp[1][0] = dp[0][0] + arr[1][0]
# dp[1][1] = dp[0][0] + arr[1][1]

for i in range(1, n):
    for j in range(i+1):
        #삼각형의 왼쪽 끝일때
        if j == 0 :
            dp[i][j] = dp[i-1][0] + arr[i][j]
        #삼각형의 오른쪽 끝일때
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + arr[i][j]
        #두 경우의 수중에 max값 dp에 넣기
        else:
            dp[i][j] = max(dp[i-1][j-1] + arr[i][j], dp[i-1][j] + arr[i][j])

#마지막 줄에서 최대값 출력
print(max(dp[n-1]))

# dp를 사용하지 않을 경우: 완전탐색
# 모든 경로를 재귀or dfs로 탐색하면서 최대합을 구해야함 각 줄마다 선택지는 2개
# 각 줄마다 갈 수 있는 선택지는 2개 총 경로의 수는 2^(n-1) 개
#따라서 시간 복잡도는 O(2^n)

#DP를 사용하는 경우
#모든 칸에 대해 한번씩만 계산 == 칸개수 만큼의 시간이 걸림
#삼각형의 총 개수는 n(n+1)/2 즉 시간 복잡도는 O(n^2)