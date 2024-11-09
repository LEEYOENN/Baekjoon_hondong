n = int(input())
arr = list(map(int, input().split()))
#print(arr)

def is_it_mountain(arr, n) :
    
    for i in range(n-1):
        ##뒤에 같은 숫자가 나오면 NO
        if arr[i] == arr[i + 1] : return 'NO'
        ##뒤에 더 작은 숫자가 나오면 일단 break
        if arr[i] > arr[i + 1] :
            break
    ##만약에 멈춘지점이 배열을 다 돈 시점이면 YES
    if i == n - 2 :
        return 'YES'
    else :
        ##멈춘지점부터 만약 다시 커지는 지점이 있으면 NO
        for j in range(i+2, n-1) :
            if arr[j] < arr[j+1] :
                return 'NO'
    ##그대로 끝까지 작아지면 YES
    return 'YES'
            

print(is_it_mountain(arr, n))