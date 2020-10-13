import sys
from collections import deque
N = 5
matrix = [[] for _ in range(N)]
for i in range(N):
    matrix[i] = list(sys.stdin.readline().split())

dir_x, dir_y = [-1, 0, 0, 1], [0, -1, 1, 0]
num_set = set()

def bfs(sx, sy):
    queue = deque()
    queue.append([[sx, sy], matrix[sx][sy]])

    while queue:
        [x, y], value = queue.popleft()
        if len(value) == 6:
            num_set.add(value)
        else:
            for i in range(4):
                dx, dy = x + dir_x[i], y + dir_y[i]
                if 0 <= dx < N and 0 <= dy < N:
                    queue.append([[dx, dy], value + matrix[dx][dy]])
for i in range(N):
    for j in range(N):
        bfs(i, j)
print(len(num_set))
