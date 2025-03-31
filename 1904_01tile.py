import sys

n = int(sys.stdin.readline().strip())

# f(n-2)와 f(n-1)의 값을 저장할 변수
prev2 = 1  # f(1)
prev1 = 2  # f(2)

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for _ in range(3, n + 1):
        curr = (prev1 + prev2) % 15746
        prev2, prev1 = prev1, curr  # 값 업데이트

    print(prev1)  # f(n) 출력