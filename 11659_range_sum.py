import sys
input = sys.stdin.readline

prefix_sum = []
n, m = map(int, input().split())
nums = list(map(int, input().split()))
allsum = [0]
mysum = 0

for i in range(n) :
    mysum += nums[i]
    allsum.append(mysum)
    
for i in range(m) :
    a, b = map(int, input().split())
    print(allsum[b] - allsum[a-1])
