numOfStrokes = [ 3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
N, M = map(int, input().split(' ')) 
name1, name2 = input().strip().split(' ')

fullName = []
if (N >= M) :
    for i in range(M) :
        fullName.append(name1[i])
        fullName.append(name2[i])
        
    for i in range(M, N) :
        fullName.append(name1[i]) 
else :
    for i in range(N) :
        fullName.append(name1[i])
        fullName.append(name2[i])

    for i in range(N, M) :
        fullName.append(name2[i]) 

fullNum = []
for i in fullName :
    fullNum.append(numOfStrokes[ord(i) - ord('A')])

while len(fullNum) > 2:
    newFullNum = []
    for i in range(len(fullNum) - 1) :
        currNum = (fullNum[i] + fullNum[i + 1]) % 10
        newFullNum.append(currNum)
    fullNum = newFullNum

result_per = fullNum[0] * 10 + fullNum[1]
print(f"{result_per}%")