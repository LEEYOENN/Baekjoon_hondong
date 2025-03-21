n = int(input())

nums = [ int(input()) for _ in range(n)]
sort_nums = sorted(nums)
print(sort_nums)
[ print(n) for n in sort_nums]