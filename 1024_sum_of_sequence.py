# 0 <  N< 1,000,000,000 , 2 <= L <= 100
#n, l = map(int, input().split())
# finish = False
# rslt = []

# for i in range(n // l , 0, -1) :
#     if finish :
#         break
#     total = 0
#     j = i
#     rslt = []
#     while total < n and j > 0 :
#         total += j
#         rslt.append(j)
#         j -= 1
#         if (j == 0 and len(rslt) == l - 1) :
#             rslt.append(0)
#         if total == n and 100 >= len(rslt) >= l :
#             rslt = rslt[::-1]
#             for num in rslt :
#                 print(num, end=' ')
#             finish = True
#             break

# if sum(rslt) != n or len(rslt) < l or len(rslt) > 100 :
#     print(-1)

# 0 <  N< 1,000,000,000 , 2 <= L <= 100
n, l = map(int, input().split())

rslt = []
for i in range(l, 101) :
    ix = n - (i*(i+1) // 2)
    if ix % i == 0 :
        x = ix // i
        if x + 1 >= 0 :
            print(*(i for i in range(x + 1, x + i + 1)))
            break
else:
    print(-1)
            
