def solution(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            # 짝이 맞으므로 스택에서 여는 괄호 제거
            stack.pop()

    return len(stack) == 0

