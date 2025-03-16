n, B = input().split()
B = int(B)

##print(int(n, B)) ##파이썬 내장 함수로 간단하게 가능

rslt = 0 #변환된 10진법 값을 저장할 변수
power = 0 #B의 지수(자리수)

#숫자를 오른쪽부터 처리
for i in reversed(n):
    if '0' <= i <= '9':
        num = ord(i) - ord('0') #문자 '0'을 빼서 본래 숫자만 남김
    else:
        num = ord(i) - ord('A') + 10 # 알파벳이라면 'A'를 빼고 10을 더해줌
    
    rslt += num * (B ** power) #B의 파워승 만큼 곱해서 자리수 반영영
    power += 1 #위 자리수로 이동
    
print(rslt)