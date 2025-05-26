import sys
input = sys.stdin.readline

n, k = map(int, input().split())

temp = list(map(int, input().split()))

hap = [0] * (n - k + 1)

for i in range(n - k + 1):
    for j in range(i, i + k):
        hap[i] += temp[j]
        
print(max(hap))