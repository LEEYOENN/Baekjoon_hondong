t = int(input())
reminder = 0

for _ in range(t):
    rslt = []
    cent = int(input())
    
    rslt.append(cent // 25) ##25센트 몇개인지 저장
    cent = cent % 25 
    
    rslt.append(cent // 10) #10센트 몇개인지 저장
    cent = cent % 10

    rslt.append(cent // 5) #5센트 몇개인지 저장
    cent = cent % 5  
    
    rslt.append(cent) #1센트 몇개인지 저장
    
    for i in rslt:
        print(i, end=" ")
    print()