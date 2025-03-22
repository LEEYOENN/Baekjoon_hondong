import sys
def heapify(arr, arr_len):
    """배열 arr를 인덱스 0 부터 인덱스 (arr_len -1) 사이를 최대 힙으로 재구성한다."""
    last_parent = arr_len // 2 - 1
    for current in range(last_parent, -1, -1):
        while current <= last_parent:
            child = current * 2 + 1
            sibling = child + 1
            if sibling < arr_len and arr[child] < arr[sibling]:
                child = sibling
            if arr[current] < arr[child]:
                arr[current], arr[child] = arr[child], arr[current]
                current = child
            else: break

def heap_sort(arr):
    """배열 arr를 오름차순으로 힙 정렬하다. """
    for arr_len in range(len(arr), 1, -1):
        heapify(arr, arr_len)
        arr[arr_len - 1], arr[0] = arr[0], arr[arr_len - 1]
        
n = int(input())

nums = [ int(sys.stdin.readline()) for _ in range(n)]
heap_sort(nums)

[ print(n) for n in nums]
    