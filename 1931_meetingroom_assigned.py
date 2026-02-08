import sys
# 입력 속도를 빠르게 하기 위해 사용
input = sys.stdin.readline

n = int(input())

meeting = []

for _ in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))


meeting.sort(key=lambda x: (x[1], x[0]))

end_time = 0
cnt = 0

for start, end in meeting:
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)