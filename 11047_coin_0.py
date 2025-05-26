import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
[ coins.append(int(input())) for _ in range(n) ]

coins.sort(reverse=True)

rslt = 0

for coin in coins:
    if k >= coin:
        rslt += k // coin
        k %= coin
        if k <= 0:
            break
print(rslt)