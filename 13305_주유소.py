n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

total_cost = 0
min_price = prices[0]

for i in range(n - 1):
    # 지금까지 중 가장 싼 주유소 가격으로 이동
    total_cost += min_price * distances[i]
    # 현재 도시 가격이 더 싸면 갱신
    if prices[i + 1] < min_price:
        min_price = prices[i + 1]

print(total_cost)