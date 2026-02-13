import heapq

def solution(nums, k):
    heap = []
    
    for num in nums:
        # 힙에 숫자를 넣음 (기본적으로 최소 힙)
        heapq.heappush(heap, num)
        
        # 힙의 크기가 k개를 넘어가면
        if len(heap) > k:
            # 가장 작은 수를 제거 (결국 큰 수 k개만 남게 됨)
            heapq.heappop(heap)
            
    # k개 중 가장 작은 값 (= 전체에서 k번째로 큰 값) 반환
    return heapq.heappop(heap)

# 팁: 파이썬 내장 함수를 쓴다면 아래 한 줄로도 가능합니다.
# return sorted(nums, reverse=True)[k-1]