from collections import deque

n = int(input())

q = deque(range(1, n + 1))

while len(q) > 1:
    q.popleft()          # 맨 위 카드 pop
    q.append(q.popleft())  # 그 다음 카드를 맨 아래로

print(q[0])