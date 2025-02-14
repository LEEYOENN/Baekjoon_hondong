
t = int(input())

for i in range(t) :
    inOutCnt = 0
    #출발점점  #도착점
    x1, y1, x2, y2 = map(int, input().strip().split())
    #행성의 개수
    n = int(input())   
    
    for j in range(n) :
        cx, cy, r = map(int, input().strip().split())
        
        dist_with_start = (((cx - x1)**2) + ((cy - y1)**2))**(1/2)
        dist_with_destination = (((cx - x2)**2) + ((cy - y2)**2))**(1/2)
        
        #원의 중점과 출발지와의 거리와 도착점과의 거리리
        print(dist_with_start, dist_with_destination)
        
        if(dist_with_start < r and dist_with_destination < r) :
            continue
        elif (dist_with_start < r) :
            inOutCnt += 1
        elif (dist_with_destination < r) :
            inOutCnt += 1
    print(inOutCnt)
    