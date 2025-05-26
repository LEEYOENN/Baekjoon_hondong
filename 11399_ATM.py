import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

nums.sort()
hap = [0] * n
print(nums)
for i in range(n):
    hap[i] = sum(nums[:i+1])
print(sum(hap))
    