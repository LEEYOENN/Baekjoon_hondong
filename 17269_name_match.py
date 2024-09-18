numOfStrokes = [ 3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
N, M = map(int, input().split(' ')) 
name1, name2 = input().strip().upper().split(' ')

##print(name1, name2)

# if len(name1) == 0 or len(name2) == 0:
#     exit()

fullName = []
if (len(name1) >= len(name2)) :
    for i in range(len(name2)) :
        fullName.append(name1[i])
        fullName.append(name2[i])
        
    for i in range(len(name2), len(name1)) :
        fullName.append(name1[i]) 
else :
    for i in range(len(name1)) :
        fullName.append(name1[i])
        fullName.append(name2[i])

    for i in range(len(name1), len(name2)) :
        fullName.append(name2[i]) 
##print(fullName)

# fullName을 숫자로 변환
fullNum = []
for i in fullName :
    fullNum.append(numOfStrokes[ord(i) - ord('A')])

    
##print(fullNum)
while len(fullNum) > 2:
    newFullNum = []
    for i in range(len(fullNum) - 1) :
        currNum = (fullNum[i] + fullNum[i + 1]) % 10
        newFullNum.append(currNum)
    fullNum = newFullNum

result_per = fullNum[0] * 10 + fullNum[1]
print(f"{result_per}%")