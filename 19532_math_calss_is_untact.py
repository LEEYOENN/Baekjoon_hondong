a, b, c, d, e, f = map(int, input().split())
flag = 0
for x in range (-999, 1000) :
    if flag: break
    for y in range(-999, 1000) :
        if (a*x) + (b*y) == c and (d*x) + (e*y) == f :
            print(f"{x} {y}")
            flag = 1
            break