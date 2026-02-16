import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    # p: 수행할 함수 (예: RDD)
    p = input().strip()
    n = int(input())
    # 입력받은 문자열 형태의 배열("[1,2,3]")을 파싱하여 리스트로 변환
    arr_str = input().strip()
    
    # 빈 배열일 경우의 예외 처리
    if arr_str == "[]":
        q = deque()
    else:
        # 양쪽 괄호 없애고 쉼표 기준으로 자르기
        q = deque(arr_str[1:-1].split(','))
        
    is_reverse = False # 뒤집혔는지 상태를 기록하는 플래그
    is_error = False   # 에러가 발생했는지 기록
    
    for cmd in p:
        if cmd == 'R':
            # R이 나오면 상태만 반전시킴 (실제로 뒤집지 않음)
            is_reverse = not is_reverse
        elif cmd == 'D':
            if not q: # 큐가 비어있는데 빼려고 하면 에러
                is_error = True
                break
            
            # 뒤집힌 상태라면 뒤에서 빼고, 아니면 앞에서 뺌
            if is_reverse:
                q.pop()
            else:
                q.popleft()
                
    if is_error:
        print("error")
    else:
        # 모든 연산이 끝난 후, 뒤집힌 상태라면 실제로 한 번만 뒤집어줌
        if is_reverse:
            q.reverse()
        # 문제 요구사항에 맞게 다시 문자열로 합쳐서 출력 (공백 없이)
        print("[" + ",".join(q) + "]")