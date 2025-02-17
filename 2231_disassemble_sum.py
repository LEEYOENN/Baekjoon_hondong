n = int(input())

for i in range(n//2, n+1) :
    temp = i
    sum = i
    while temp != 0 :
        sum += temp % 10
        temp = temp // 10
        
    if sum == n :
        print(i)
        break
else:
    print(0)