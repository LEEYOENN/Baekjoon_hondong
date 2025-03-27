# n과 m 입력받기
n, m = map(int, input().split())
# n * m 크기의 B or W 배열 입력받기
board = [input().strip() for _ in range(n)]
#print(board)

#min_cnt = 999999

#초기 mincnt값을 충분히 큰값으로 설정정
min_cnt = float('inf')

#모든 가능 시작점에 대한 반복문
for i in range(n - 7):
    for j in range(m - 7):
        cntW = 0  # 'W'로 시작하는 체스판으로 만들기 위한 변경 횟수
        cntB = 0  # 'B'로 시작하는 체스판으로 만들기 위한 변경 횟수
        x, y = 1, 1
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if x % 2 == 1:
                    if y % 2 == 1 and board[k][l] != "W":
                        cntW += 1
                    elif y % 2 == 1 and board[k][l] != "B":
                        cntB += 1
                    elif y % 2 == 0 and board[k][l] != "B":
                        cntW += 1
                    elif y % 2 == 0 and board[k][l] != "W":
                        cntB += 1
                else:
                    if y % 2 == 1 and board[k][l] != "B":
                        cntW += 1
                    elif y % 2 == 1 and board[k][l] != "W":
                        cntB += 1
                    elif y % 2 == 0 and board[k][l] != "W":
                        cntW += 1
                    elif y % 2 == 0 and board[k][l] != "B":
                        cntB += 1
                y += 1
            x += 1
         
        #최소합을 찾아서 min_cnt에 넣음음   
        min_cnt = min(min_cnt, cntW, cntB)           
            
 #정답출력력           
print(min_cnt)

                    
                