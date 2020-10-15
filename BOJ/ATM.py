import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

total = 0
ret = 0
for value in arr:
    total += value
    ret += total
print(ret)