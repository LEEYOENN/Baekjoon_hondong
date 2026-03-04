from collections import deque

def last_card(n):
    queue = deque(range(1, n+1))

    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft()) # 뒤로 이동

    return queue[0]