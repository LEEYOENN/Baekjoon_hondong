#최소 분해합을 찾고싶은 수를 입력받음
n = int(input())

#반보다 작은 분해합은 없다고 판단해서 n/2 부터 시작작
for i in range(n//2, n+1) :
    temp = i #분해할 temp변수 만듦
    sum = i #먼저 자기자신을 sum에 넣고
    while temp != 0 :
        sum += temp % 10 #분해합을 sum에 더한다다
        temp = temp // 10
        
    if sum == n : #분해합이 n과같으면 출력후 break
        print(i)
        break
else:
    print(0)