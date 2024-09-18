file_num = int(input())
pattern = input().strip()

pat1, pat2 = pattern.split('*')

files = []
for i in range(file_num):
    file = input()
    files.append(file)

rslt = []
    
for i in files :
    if len(i) >= ( len(pat1) + len(pat2) ) :
        if (i[:len(pat1)] == pat1) and ( i[-len(pat2):] == pat2 ) :
            rslt.append("DA")
        else : rslt.append("NE")
    else :
        rslt.append("NE")
        continue
for i in rslt :
    print(i)
