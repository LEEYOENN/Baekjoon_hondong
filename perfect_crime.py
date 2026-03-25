import sys
import ast

input = sys.stdin.readline

def solution(info, n, m):
    
    dp = [float('inf')] * n

    dp[0] = 0
    
    for a_trace, b_trace in info:
        new_dp = [float('inf')] * n
        
        for i in range(n):
            if dp[i] == float('inf'):
                continue
            
            if i + a_trace < n:
                new_dp[i + a_trace] = min(dp[i], new_dp[i+a_trace])
            
            if dp[i] + b_trace < m:
                new_dp[i] = min(new_dp[i], dp[i] + b_trace)
                                 
        dp = new_dp
        
    for i in range(n):
        if dp[i] < m:
            return i
    
    return -1

    answer = 0

    return answer

# user_input = input()
# n = int(input())
# m = int(input())

# info = list(ast.literal_eval(user_input))

# print(solution(info, n, m))