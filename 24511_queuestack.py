import sys
input = sys.stdin.readline
from collections import deque
N = int(input()) ##자료구조 개수
A = list(map(int, input().split())) #큐인지 스택인지
B = list(map(int, input().split())) #자료구조 초기 값

M = int(input()) #새로 입력할 값 개수
C = list(map(int, input().split())) #새로 입력할 값

# A[i] == 0인 위치에 있는 값만 뽑아와서 별도 deque로 저장
qstack = deque([B[i] for i in range(N) if A[i] == 0])

rslt = []

## 자료구조가 STACK인 부분은 변하지 않아서 무의미하다
# 각 num을 큐스택에 넣고 맨 뒤 값만 꺼낸다다
for num in C:
    qstack.appendleft(num)
    rslt.append(qstack.pop())
    
sys.stdout.write(" ".join(map(str, rslt)) + " ")


##Queue인 인덱스만 뽑아서 - 시간초과
# zero_idx = [ i for i in range(N) if A[i] == 0 ]

# result = []

# for num in C:
#     temp = num
#     for i in zero_idx:
#         temp, B[i] = B[i], temp
#     result.append(temp)

#전체 이중반복문 돌면서 - 시간초과
# sys.stdout.write(" ".join(map(str, result)) + " ")
# for j in range(M):
#     num = C[j]
#     for i in range(N):
#         if A[i] == 0:
#             temp = B[i]
#             B[i] = num
#             num = temp
#         elif A[i] == 1:
#             continue
#      print(num)      