n,m = map(int, input().split())

lights = (list(map(int, input().split())))
print(lights)

for i in range(m):
    method, l, r = map(int, input().split())
    if method == 1:
        lights[l-1] = r
        
    elif method == 2:
        for j in range(l-1, r) :
            lights[j] = (lights[j] -1) ** 2
    elif method == 3:
        for j in range(l-1, r) :
            lights[j] = 0
    elif method == 4:
        for j in range(l-1, r) :
            lights[j] = 1

for i in lights:
    print("%d" %(i), end=" ")