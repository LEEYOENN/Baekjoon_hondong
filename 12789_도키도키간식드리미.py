def can_get_snacks(n, students):
    stack = []
    order = 1
    for student in students:
        while stack and stack[-1] == order:
            stack.pop()
            order += 1
        if student == order:
            order += 1
        else:
            stack.append(student)

    # 남은 스택도 검사
    while stack and stack[-1] == order:
        stack.pop()
        order += 1

    return "Nice" if not stack else "Sad"


# 입력 처리
n = int(input())
students = list(map(int, input().split()))

# 결과 출력
print(can_get_snacks(n, students))
