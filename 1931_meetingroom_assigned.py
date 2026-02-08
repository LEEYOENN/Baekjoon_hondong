import sys
# 입력 속도를 빠르게 하기 위해 사용
input = sys.stdin.readline

n = int(input())

meeting = []

for _ in range(n):
    # 시작 시간(s), 끝나는 시간(e) 입력받아 리스트에 추가
    s, e = map(int, input().split())
    meeting.append((s, e))