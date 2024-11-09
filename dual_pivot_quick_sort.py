import random
import time
import matplotlib.pyplot as plt

def dual_pivot_quick_sort(arr, left, right, threshold) :
    if (right - left + 1) <= threshold :
        insertion_sort(arr, left, right)
    elif left >= right :
        return
    else : 
        lp, rp = partition(arr, left, right)
        dual_pivot_quick_sort(arr, left, lp -1, threshold)
        dual_pivot_quick_sort(arr, lp + 1, rp - 1, threshold)
        dual_pivot_quick_sort(arr, rp + 1, right, threshold)
        

def partition(arr, left, right) :
    if arr[left] > arr[right] :
        tmp = arr[left]
        arr[left] = arr[right]
        arr[right] = tmp
        
    l_pivot = arr[left]
    r_pivot = arr[right]
    
    lt = left +1
    gt = right - 1
    i = lt
    
    while i <= gt :
        if arr[i] < l_pivot : ##left pivot보다 작은값 처리
            tmp = arr[i]
            arr[i] = arr[lt]
            arr[lt] = tmp
            
            lt += 1
            i += 1
        elif arr[i] > r_pivot : ## right pivot보다 큰 값 처리
            tmp = arr[i]
            arr[i] = arr[gt]
            arr[gt] = tmp
            
            gt -= 1
        elif l_pivot <= arr[i] <= r_pivot : # l_pivot r_pivot 둘 사이값 처리
            i+=1
            
    arr[left], arr[lt - 1]  = arr[lt -1], arr[left] ##left를 lp보다 작은값들의 끝으로
    arr[right], arr[gt + 1] = arr[gt + 1], arr[right] #right를 rp보다 큰값들의 처음으로

    return lt - 1, gt + 1

def insertion_sort(arr, left, right) :
    for i in range(left + 1, right + 1) :
        key = arr[i]
        j = i - 1 ##키의 바로 왼쪽
        
        while j >= left and arr[j] > key :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
    

thresholds = [17, 33, 65, 129, 257, 513]
arr_sizes = [10_000, 100_000, 200_000, 400_000, 800_000, 1_600_000, 3_200_000, 6_400_000]

## 결과를 저장할 딕셔너리 생성 {17: [], 33:[], 65:[], 129:[], 257:[], 513:[]}이렇게 만들어짐
results = {threshold: [] for threshold in thresholds}

## 수행시간 저장 time 라이브러리 사용
# 바깥에서 sizes에 맞춰 반복
for size in arr_sizes:
    arr = random.sample(range(size), size)  # 새로운 랜덤 배열 생성
    for threshold in thresholds :
        arr_cpy = arr.copy() ## thresholds를 반복할동안 arr이 보존하기위한 코드
        start_time = time.time()
        dual_pivot_quick_sort(arr_cpy, 0, len(arr_cpy)-1, threshold)
        end_time = time.time()
        
        # 수행시간을 현재 threshold 키값에 맞는 곳에 append
        results[threshold].append(end_time - start_time)
        print(f"Array Size: {size}, Threshold: {threshold},Time: {end_time - start_time:.4f} sec")

# 그래프 출력
colors = ['red', 'orange', 'gold', 'green', 'blue', 'violet', 'k']
i = 0
plt.figure(figsize=(10, 6))
for threshold in thresholds:
    plt.plot(arr_sizes, results[threshold], color=colors[i], label=f'Threshold = {threshold}', marker='o')
    i += 1
plt.xlabel('Length of Array')
plt.ylabel('Time(second)')
plt.title('Dual Pivot + Vladimir Sort')
plt.legend()
plt.grid(True)
plt.show()