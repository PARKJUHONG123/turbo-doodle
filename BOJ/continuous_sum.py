import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
A, B = [], []

for value in arr:
    if not A:
        A.append(value)
        B.append(value)
        continue

    if value > 0:
        A.append(max(A[-1] + value, value))
        B.append(max(B[-1] + value, value))

    else:
        B.append(max(max(B[-1] + value, A[-1]), value))
        A.append(max(A[-1] + value, value))

print(max(max(A), max(B)))
