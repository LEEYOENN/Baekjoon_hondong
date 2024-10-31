n = int(input())
cost = []
for i in range(n):
    price = int(input())
    cost.append(price)
    

cost.sort(reverse=True)
##print(cost)

rslt = 0
# rest = len(cost) % 3

# idx = 0
# for i in range(len(cost)-rest) :
#     if (i+1) % 3 != 0 :
#         rslt += cost[i]

# for j in range(rest) :
#     rslt += cost[i + j]

for i in range(len(cost)) :
    rslt += cost[i]
    if (i+1) % 3 == 0 :
        rslt -= cost[i]
print(rslt)