n = int(input())
cnt = 0 #그룹단어를 카운트할 변수

for _ in range(n):
    flag = 1 # 확인한 단어가 그룹단어였는지 확인할 변수수
    word = input()
    seen_chars = set() # 등장한 문자를 저장할 set
    prev_char = '' #연속된 문자인지 확인할 전글자 변수수
    
    seen_chars.add(word[0])
    prev_char = word[0] 
    
    for i in word :
        if i == prev_char:
            continue
        else:
            if i in seen_chars:
                flag = 0
                break
            else:
                seen_chars.add(i)
                prev_char = i
    if flag:
        cnt += 1
        
print(cnt)
            