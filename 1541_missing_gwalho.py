import sys
input = sys.stdin.readline

expression = input()

split_minus = expression.split('-')

rslt = 0

x = sum(map(int, (split_minus[0].split('+'))))

if expression[0] == '-' :
    rslt -= x
else :
    rslt += x

for x in split_minus[1:] :
    mysum = sum(map(int, x.split('+'))) 
    
    rslt -= mysum
    
print(rslt)