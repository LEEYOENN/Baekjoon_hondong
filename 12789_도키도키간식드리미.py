n = int(input())
line = list(map(int, input().split()))
stack = []
next_num = 1

for firstStudent in line:
    stack.append(firstStudent)
    # 스택의 top이 next_num과 같으면 pop
    while stack and stack[-1] == next_num:
        stack.pop()
        next_num += 1

# 모든 학생이 순서대로 간식 받았으면 스택은 비어 있음
if not stack:
    print("Nice")
else:
    print("Sad")


# 간식을 받을 수 있는 경우는 줄에서만이 아니라, 줄과 스택을 동시에 고려하면서 진행되어야 합니다.
#즉, 줄에서 학생을 하나씩 볼 때마다, 스택의 맨 위가 next_num이면 스택에서 먼저 꺼내줘야 해요.
# # 입력 처리
# n = int(input())
# line = list(map(int, input().split()))

# stack = []
# next_num = 1
# for student in line:
#     if student == next_num:
#         next_num += 1
#     else:
#         stack.append(student)

# # 남은 스택도 검사
# while stack:
#     top = stack.pop()
#     if top == next_num:
#         next_num += 1
#     else: 
#         print("Sad")
#         break
# else:
#     print("Nice")