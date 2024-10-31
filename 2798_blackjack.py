from itertools import permutations

N, M = map(int, input().split())
nums = map(int, input().split())

sums = list(permutations(nums, 3))

max_sum = 0
for i in sums :
    if (sum(i) > max_sum) and (sum(i) <= M):
        max_sum = sum(i)
print(max_sum)
