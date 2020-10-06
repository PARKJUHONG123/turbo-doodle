import sys
from collections import deque
dir_x = [1, 0, -1, 0]
dir_y = [0, -1, 0, 1]

N = int(sys.stdin.readline())
point = set()

for _ in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split())
    stack = list()
    stack.append(d)

    for i in range(1, g + 1):
        length = 2 ** i - 2 ** (i - 1)
        for j in reversed(range(length)):
            value = stack[j]
            stack.append((value + 1 if value < 3 else 0))

    point.add((x, y))
    for i in stack:
        x, y = x + dir_x[i], y + dir_y[i]
        point.add((x, y))

count = 0
for value in point:
    px, py = value
    a, b, c = (px, py + 1), (px + 1, py), (px + 1, py + 1)
    if a in point and b in point and c in point:
        count += 1
print(count)