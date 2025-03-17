N, B = map(int, input().split())

rslt = '' #마지막에 출력할 결과
while N > 0 :
    rest = N % B #나머지 구하기
    if rest >= 10 : # 나머지가 10 이상이면 알파벳으로
        rslt += chr(rest - 10 + ord('A'))
    else: #0~9는 그대로
        rslt += str(rest)
    N = N // B # N 없데이트
    
print(rslt[::-1])