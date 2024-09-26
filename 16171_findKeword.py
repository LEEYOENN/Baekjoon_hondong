str = input()
keyword = input()

alpha = ''

for i in str :
     if '0' <= i <= '9':
         continue
     else :
         alpha += i
         
if keyword in alpha :
    print(1)
else :
    print(0)
