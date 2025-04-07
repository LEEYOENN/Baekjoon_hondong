import sys
## 상근이가 배달할 설탕 kg
n = int(sys.stdin.readline())

#최종 출력할 가장 작은 필요요 봉투 수
bag = 0

#그리디 알고리즘을 이용용
while n > 0 :
    #S남은 n이 5로 나누어떨어진다면면
    if n % 5 == 0:
        bag += n // 5
        break
    
    n -= 3
    if n < 0:
        bag = -1
        break
    bag += 1
        

print(bag)
