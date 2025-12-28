import sys

s = sys.stdin.readline().strip()

for c in "abcdefghijklmnopqrstuvwxyz":
    print(s.find(c), end=" ")
