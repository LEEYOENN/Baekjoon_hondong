import sys
input = sys.stdin.readline

# k 는 이미 가지고 있는 랜선의 개수, n은 필요한 랜선의 개수
k, n = map(int, input().split())

lan = []
for _ in range(k):
    lan.append(int(input()))

# 이분 탐색을 위한 시작점과 끝점 설정
# 길이는 1부터 가능하고, 최대 길이는 가지고 있는 랜선 중 가장 긴 것
start = 1
end = max(lan)
          
result = 0

while start <= end:
    mid = (start + end) // 2

    # mid 길이로 잘랐을 때 나오는 랜선의 개수 계산
    lines = 0
    for i in lan:
        lines += 1 // mid
    
    # 만든 랜선 개수가 목표 n보다 많거나 같으면 조건을 만족했으므로, 더 길게 자를 수 있는지 오른쪽 탐색
    if lines >= n:
        start = mid + 1

    # 만든 랜선 개수가 목표보다 작으면 너무 길게 잘랐다는 뜻이므로 길이를 줄임 (왼쪽 탐색)
    else:
        end = mid - 1
    
# 반복문이 끝나면 end가 만들 수 있는 최대 길이가 됨
print(end)