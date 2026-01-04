x = int(input())
n = int(input())

total = 0
for _ in range(n):
    price, cnt = map(int, input().split())
    total += price * cnt

print("Yes" if total == x else "No")