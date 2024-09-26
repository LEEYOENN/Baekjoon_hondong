from itertools import permutations

n = int(input())

nums = list(permutations(list(range(1, 10)), 3))

def calc_strike_ball(guess, answer) :
    cnt_s, cnt_b = 0, 0
    for i in range(3) :
        if guess[i] == int(answer[i]) :
            cnt_s += 1
        elif str(guess[i]) in answer :
            cnt_b += 1
    return cnt_s, cnt_b

input_line = []

for i in range(n) :
    answer, stk, ball = input().split()
    stk = int(stk)
    ball = int(ball)
    
    input_line.append((answer, stk, ball))

for answer, stk, ball in input_line :
    nums = [num for num in nums if calc_strike_ball(num, answer) == (stk, ball)]
    

print(len(nums))