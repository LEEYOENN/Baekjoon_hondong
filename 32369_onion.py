compliOnion = 1
blameOnion = 1

n, a, b = map(int, input().split())

for i in range(n):
    compliOnion += a
    blameOnion += b
    ##비난 양파가 칭찬양파보다 더 길어지면
    if(blameOnion > compliOnion) :
        tmp = compliOnion
        compliOnion = blameOnion
        blameOnion = tmp
        
    elif (blameOnion == compliOnion) :
        blameOnion -= 1
        
print(f'{compliOnion} {blameOnion}')
        