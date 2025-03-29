import sys
## 상근이가 배달할 설탕 kg
n = int(sys.stdin.readline())

#최종 출력할 가장 작은 봉투 수수
bag = 0
while n >= 0 :
    if n % 5 == 0:
        bag += n // 5
        break
    n -= 3
    if n < 0:
        bag = -1
        break
    bag += 1
        

print(bag)


# if n % 5 == 0 :
#     cnt += n // 5
# else :
#     reminder = n % 5
#     cnt += n // 5

#     if reminder % 3 == 0 :
#         cnt += reminder // 3
#     else:
#         cnt = -1
