import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

cards = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

counts = Counter(cards)

for target in targets:
    print(counts[target], end=' ')