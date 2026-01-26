import sys
input = sys.stdin.readline

n = int(input())
cost = []

for _ in range(n):
    cost.append(list(map(int, input().split())))

# cost[i][0]: 빨강, cost[i][1]: 초록, cost[i][2]: 파랑
# i번째 집을 특정 색으로 칠할 때의 누적 최소 비용을 바로 덮어쓰기(Memoization)
for i in range(1, n):
    # i번째 집을 '빨강'으로 칠하려면? 
    # 바로 전 집(i-1)은 '초록'이나 '파랑' 중 더 비용이 싼 곳을 선택했어야 함
    cost[i][0] += min(cost[i-1][1], cost[i-1][2])
    
    # i번째 집을 '초록'으로 칠하려면?
    # 전 집은 '빨강'이나 '파랑'이어야 함
    cost[i][1] += min(cost[i-1][0], cost[i-1][2])
    
    # i번째 집을 '파랑'으로 칠하려면?
    # 전 집은 '빨강'이나 '초록'이어야 함
    cost[i][2] += min(cost[i-1][0], cost[i-1][1])

# 마지막 집(n-1)까지 칠했을 때, 세 가지 색 중 비용이 가장 작은 값 출력
print(min(cost[n-1]))