import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    stack = []
    a = input().strip()
    is_vps = True # 올바른 괄호 문자열(VPS)인지 판단하는 플래그

    for char in a:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack: # 스택에 여는 괄호가 있다면 짝을 맞춰 제거
                stack.pop()
            else: # 스택이 비어있는데 닫는 괄호가 나오면 에러
                is_vps = False
                break
    
    # 반복문이 끝난 후 스택이 비어있지 않다면(여는 괄호가 남음) 에러
    if not stack and is_vps:
        print("YES")
    else:
        print("NO")