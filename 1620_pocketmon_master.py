import sys
input = sys.stdin.readline

# n: 도감에 수록된 포켓몬 수, m: 맞춰야 하는 문제 수
n, m = map(int, input().split())

# 이름으로 번호를 찾을 딕셔너리
name_to_id = {}
# 번호로 이름을 찾을 딕셔너리
id_to_name = {}

for i in range(1, n + 1):
    name = input().strip()
    name_to_id[name] = i
    id_to_name[i] = name

for _ in range(m):
    query = input().strip()
    
    # 입력이 숫자인지 문자인지 판별
    if query.isdigit():
        # 숫자면 이름을 출력
        print(id_to_name[int(query)])
    else:
        # 문자면 번호를 출력
        print(name_to_id[query])