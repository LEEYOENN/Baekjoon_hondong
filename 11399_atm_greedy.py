import sys
input = sys.stdin.readline

# N: 사람의 수
n = int(input())

# P: 각 사람이 돈을 인출하는 데 걸리는 시간 리스트
people = list(map(int, input().split()))

# 시간이 적게 걸리는 사람이 먼저 인출해야 뒷사람의 대기 시간이 줄어듦
# 따라서 오름차순 정렬이 핵심 로직
people.sort()

total_time = 0   # 총 걸린 시간의 합
current_wait = 0 # 각 사람이 기다리고 인출하는 데 걸린 누적 시간

for time in people:
    # 이전 사람들의 시간 + 내 시간
    current_wait += time 
    # 총 합계에 더하기
    total_time += current_wait

print(total_time)