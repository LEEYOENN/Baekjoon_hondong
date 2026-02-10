def solution(nums, target):
    num_map = {}

    for i, num in enumerate(nums):
        # 목표값에서 현재 값을 뺀 수가 딕셔너리에 있는지 확인
        need_num = target - num

        if need_num in num_map:
            # 있다면 필요 수의 인덱스, 현재 수의 인덱스] 반환
            return [num_map[need_num], i]
        
        # 없다면 현재 숫자의 인덱스를 딕셔너리에 저장
        num_map[num] = i
    
    return []

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(solution(nums, target))