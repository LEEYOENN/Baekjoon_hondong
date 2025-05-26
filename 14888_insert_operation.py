import sys
input = sys.stdin.readline
# 숫자의 개수 n 을 입력받습니다.
n = int(input())
## 두 번째 줄: 수열 A1, A2, ..., An을 리스트로 입력받습니다.
number = list(map(int, input().split()))
##연산자의 각 개수를 입력받습니다. 합은 언제가 n-1개개
add, sub, mul, div = map(int, input().split())
##최댓값 초기화
max_result = - int(1e9)
##최솟값 초기화
min_result = int(1e9)

##dfs: 깊이 우선 탐색으로 가능한 모든 수식 조합을 탐색
#add, sub, mul, div: 남은 연산자 개수
#sum: 지금까지 계산된 결과값
#idx: 현재 처리 중인 number 리스트의 인덱스 (몇 번째 숫자인지)
def dfs(add, sub, mul, div, sum, idx):
    ##전역변수(max_result, min_result)에 접근하여 값을 갱신하기 위해 global 선언
    global max_result, min_result
    #수열의 마지막까지 탐색을 마쳤다면면
    if idx == n:
        #계산되어 넘어온 sum 값을 현재 최댓값, 최솟값과 비교해서 갱신
        #종료 조건에 도달했으므로 return
        max_result = max(max_result, sum)
        min_result = min(min_result, sum)
        return
    #만약 + 연산자가 하나이상 남아있다면 add 하나 차감하고 sum에 다음 숫자를 더하고 다음 인덱스로 이동해서 dfs 호출
    if add:
        dfs(add-1, sub, mul, div, sum + number[idx], idx + 1)
    #만약 - 연산자가 하나이상 남아있다면 sub 하나 차감하고 sum에 다음 숫자를 빼고 다음 인덱스로 이동해서 dfs 호출
    if sub:
        dfs(add, sub-1, mul, div, sum - number[idx], idx + 1)
    #만약 x 연산자가 하나이상 남아있다면 mul 하나 차감하고 sum에 다음 숫자를 곱하고 다음 인덱스로 이동해서 dfs 호출
    if mul:
        dfs(add, sub, mul-1, div, sum * number[idx], idx + 1)
    #만약 / 연산자가 하나이상 남아있다면 div 하나 차감하고 sum에 다음 숫자를 나누고고 다음 인덱스로 이동해서 dfs 호출
    if div:
        dfs(add, sub, mul, div-1, int(sum / number[idx]), idx + 1)
        
## 처음 dfs 메서드 호출 두번째 숫자부터 탐색
dfs(add, sub, mul, div, number[0], 1)
print(max_result)
print(min_result)

# 백트랙킹은 dfs와 비슷하지만 굳이 분리해서 의미부여를 하면 끝까지 가느냐 돌아오느냐로 간단하게 생각할수 있음
# 백트랙킹은 현재가는 길이 더이상해가 아니라고 판단되면 되돌아오는것