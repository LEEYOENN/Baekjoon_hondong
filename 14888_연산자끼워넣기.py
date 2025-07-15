import sys

input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split())) #수열 A1 ~An

plus, minus, multiply, divide = map(int, input().split()) #연산자 개수

#결과 최댓값과 최솟값을 저장할 전역 변수
max_result = -1e9
min_result = 1e9

# DFS 함수 정의
def dfs(idx, result, plus, minus, multiply, divide):
    """
    idx: 현재 처리 중인 숫자의 인덱스
    result: 지금까지 계산된 결과값
    plus/minus/multiply/divide: 남은 각 연산자의 개수
    """

    # 종료 조건: 모든 숫자를 다 사용했을 때
    if idx == n:
        global max_result, min_result
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    # 다음 숫자
    num = numbers[idx]

    # 가능한 연산자 각각에 대해 재귀적으로 탐색
    if plus > 0:
        dfs(idx + 1, result + num, plus - 1, minus, multiply, divide)
    if minus > 0:
        dfs(idx + 1, result - num, plus, minus - 1, multiply, divide)
    if multiply > 0:
        dfs(idx + 1, result * num, plus, minus, multiply - 1, divide)
    if divide > 0:
        # 정수 나눗셈 처리:  음수 나눗셈 구현
        if result < 0:
            dfs(idx + 1, -(-result // num), plus, minus, multiply, divide - 1)
        else:
            dfs(idx + 1, result // num, plus, minus, multiply, divide - 1)

# DFS 시작: 첫 번째 숫자는 결과로 설정, 인덱스는 1부터 시작
dfs(1, numbers[0], plus, minus, multiply, divide)

# 결과 출력
print(max_result)
print(min_result)