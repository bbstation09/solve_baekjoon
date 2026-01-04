n = int(input())
arr = list(map(int, input().split()))
arr.sort()

total = 0
prefix = 0
for x in arr:
    prefix += x
    total += prefix

print(total)
