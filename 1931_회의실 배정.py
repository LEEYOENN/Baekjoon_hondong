import sys
input = sys.stdin.readline
n = int(input())

meeting = [ tuple(map(int, input().split())) for _ in range(n) ]


meeting.sort(key = lambda x: (x[1], x[0]))

count = 0
endtime = 0

for start, end in meeting:
    if start >= endtime:
        count += 1
        endtime = end
        
print(count)