import sys
from collections import deque

dir_x = [-1, 0, 1, 0]
dir_y = [0, 1, 0, -1]

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

matrix = [[False for _ in range(N)] for _ in range(N)]
for i in range(K):
    ax, ay = map(int, sys.stdin.readline().split())
    matrix[ax - 1][ay - 1] = True

x, y, dir = 0, 0, 1
L = int(sys.stdin.readline())
snake, length = deque(), 1
snake.append([x, y])

time_dict = dict()
for i in range(L):
    S, D = sys.stdin.readline().split()
    time_dict[int(S)] = D

count = 0
while True:
    count += 1
    x, y = x + dir_x[dir], y + dir_y[dir]
    if x < 0 or x >= N or y < 0 or y >= N:
        break
    if [x, y] in snake:
        break
    else:
        snake.append([x, y])
    if matrix[x][y]:
        matrix[x][y] = False
        length += 1
    if len(snake) > length:
        snake.popleft()
    if count in time_dict:
        if time_dict[count] == 'D':
            dir = (dir + 1 if dir < 3 else 0)
        else:
            dir = (dir - 1 if dir > 0 else 3)
print(count)