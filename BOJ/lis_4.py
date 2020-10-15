import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = [0]

for value in arr:
    if stack[-1] < value:
        stack.append(value)
    else:
        stack[bisect_left(stack, value)] = value

print(len(stack) - 1)