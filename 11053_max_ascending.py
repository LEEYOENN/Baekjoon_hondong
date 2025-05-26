import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
##초기값 모든 dp[i] = 1 자기 자신 하나만 있어도 길이1
dp = [1] * n

if  n == 1:
    print(1)
    
else:
    for i in range(n):
        for j in range (i):
            if nums[i] > nums[j] :
                dp[i] = max(dp[i], dp[j] + 1)
                
    print(max(dp))