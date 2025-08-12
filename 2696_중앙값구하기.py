import sys
import heapq

input = sys.stdin.readline


#두개의 힙 아이디어
#왼쪽힙(max heap) 지금까지 나온 작은 절반 저장
#오른쪽힙(min heap) 지금까지 나온 큰 절반 저장

#왼쪽 힙의 크기 == 오른쪽 힙의 크기 or
#왼쪽 힙의 크기 == 오른쪽 힙 + 1
#중앙값은 항상 왼쪽 힙의 가장 큰 값(루트)

t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    m = int(input()) # 수열 길이
    nums = []
    
    # 입력이 한줄에 10개싹 오니까 전부 이어붙여서 읽기
    while len(nums) < m:
        nums.extend(map(int, input().split()))
        
    left = [] #최대힙(파이썬은 최소 힙이라 - 붙여서 사용)
    right = [] #최소힙
    medians = []
    
    for i, x in enumerate(nums, start=1): #홀수번째 알아야되니까 start=1
        # 1) 왼쪽 힙이 비었거나 x가 왼쪽 힙 최대값보다 작거나 같으면 왼쪽 힙에
        if not left or x <= -left[0]:
            heapq.heappush(left, -x)
        else:
            heapq.heappush(right, x)

        # 2) 균형 맞추기
        if len(left) < len(right):
            heapq.heappush(left, -heapq.heappop(right))
        elif len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))

        # 3) 홀수 번째 수를 읽었을 때 중앙값 기록
        if i % 2 == 1:
            medians.append(-left[0])
            
# 출력
    print(len(medians))
    for i in range(len(medians)):
        print(medians[i], end=' ')
        if (i + 1) % 10 == 0:  # 10개씩 줄바꿈
            print()
    if len(medians) % 10 != 0:
        print()