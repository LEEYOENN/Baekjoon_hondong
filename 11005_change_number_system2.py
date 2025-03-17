N, B = map(int, input().split())

rslt = '' #마지막에 출력할 결과
while N > 0 :
    rest = N % B #나머지 구하기
    if rest >= 10 : # 나머지가 10 이상이면 알파벳으로
        rslt += chr(rest - 10 + ord('A')) #if rest == 24 면 (0~9)에 해당하는 10을 빼고 14 번째 알파벳 'N'이됨
    else: #0~9는 그대로
        rslt += str(rest)
    N = N // B # N 없데이트
    
print(rslt[::-1]) #맨끝자리부터 추가했기때문에 반대로 출력해야한다