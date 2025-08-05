N, M = map(int, input().split())

types = list(map(int, input().split()))
initial_values = list(map(int, input().split()))
values = list(map(int, input().split()))

qstack = []

for i in range(N):
    if types[i] == 0: #queue
        qstack.append([initial_values[i]])
    else: #stack
        qstack.append([initial_values[i]])
    
#입력값 하나씩 넣으면서 시뮬레이션
for value in values:
    x = value
    for i in range(N):
        #삽입
        qstack[i].append(x)
        #삭제
        if types[i] == 0: #queue
            x = qstack[i].pop(0)
        else: #stack
            x = qstack[i].pop()
            
    print(x)
            
        