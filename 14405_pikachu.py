string = input()

rslt = 'YES'
i = 0
while i < len(string):
    if string[i] == 'p' :
        if i + 1 < len(string) and string[i + 1] == 'i':
            i = i + 2
            continue
        else:
            rslt = 'NO'
            break
    elif string[i] == 'k':
        if i + 1 < len(string) and string[i + 1] == 'a':
            i = i + 2
            continue
        else:
            rslt = 'NO'
            break
    elif string[i] == 'c':
        if i + 2 < len(string) and string[i + 1] == 'h' and string[i + 2] == 'u':
            i = i + 3
            continue
        else:
            rslt = 'NO'
            break
    else:
        rslt = 'NO'
        break

   
print(rslt)