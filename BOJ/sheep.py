import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
matrix = [['' for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    tmp = sys.stdin.readline()
    for j in range(M):
        if tmp[j] == '#':
            visited[i][j] = True
        matrix[i][j] = tmp[j]

dir_x = [-1, 0, 0, 1]
dir_y = [0, -1, 1, 0]

total_sheep, total_wolf = 0, 0

def bfs(sx, sy):
    global total_wolf, total_sheep
    if visited[sx][sy]:
        return

    wolf, sheep = 0, 0
    queue = deque()
    queue.append([sx, sy])
    visited[sx][sy] = True
    if matrix[sx][sy] == 'o':
        sheep += 1
    elif matrix[sx][sy] == 'v':
        wolf += 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx, dy = x + dir_x[i], y + dir_y[i]
            if 0 <= dx < N and 0 <= dy < M:
                if not visited[dx][dy]:
                    visited[dx][dy] = True
                    value = matrix[dx][dy]
                    if value == '.':
                        queue.append([dx, dy])
                    elif value == 'o':
                        queue.append([dx, dy])
                        sheep += 1
                    elif value == 'v':
                        queue.append([dx, dy])
                        wolf += 1
    if wolf < sheep:
        total_sheep += sheep
    else:
        total_wolf += wolf

for i in range(N):
    for j in range(M):
        bfs(i, j)

print(total_sheep, total_wolf)
