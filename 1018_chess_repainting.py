# n과 m 입력받기
n, m = map(int, input().split())
# n * m 크기의 B or W 배열 입력받기
board = [input().strip() for _ in range(n)]
repainting = []

print(board)

for i in range(n - 7):
    for j in range(m - 7):
        cnt = 0
        if board[i][j] == 'W':
            for k in range(i, i + 8):
                for x in range(j, j + 8):
                    if k % 2 == 0 and x % 2 == :
                        
                    
                