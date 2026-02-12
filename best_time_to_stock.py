import sys

def solution(prices):
    # 최저가를 저장할 변수 (초기값은 아주 큰 수로 설정)
    min_price = sys.maxsize
    max_profit = 0
    
    for price in prices:
        # 1. 오늘 가격이 지금까지의 최저가보다 낮다면 갱신
        if price < min_price:
            min_price = price
        
        # 2. (오늘 가격 - 최저가)가 현재 최대 수익보다 크다면 갱신
        elif price - min_price > max_profit:
            max_profit = price - min_price
            
    return max_profit
