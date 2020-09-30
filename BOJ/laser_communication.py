import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
matrix = [['.' for _ in range(M)] for _ in range(N)]
visited = [[[0 for _ in range(4)] for _ in range(M)] for _ in range(N)]
start, end = [], []
for i in range(N):
    tmp = sys.stdin.readline()
    for j in range(M):
        if tmp[j] == 'C':
            if start:
                end = [i, j]
            else:
                start = [i, j]
        matrix[i][j] = tmp[j]

dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]

def bfs():
    ret = []
    queue = deque()
    for i in range(4):
        queue.append([start, i])
        visited[start[0]][start[1]][i] = 1
    matrix[start[0]][start[1]] = '*'
    while queue:
        [x, y], dir = queue.popleft()
        dx, dy = x + dir_x[dir], y + dir_y[dir]
        if 0 <= dx < N and 0 <= dy < M:
            if visited[dx][dy][dir] == 0 or visited[dx][dy][dir] > visited[x][y][dir]:
                if matrix[dx][dy] == '.':
                    visited[dx][dy][dir] = visited[x][y][dir]
                    queue.appendleft([[dx, dy], dir])
                    ndir = [(dir + 1) % 4, (dir + 3) % 4]
                    for value in ndir:
                        if visited[dx][dy][value] == 0 or visited[dx][dy][value] > visited[dx][dy][dir] + 1:
                            visited[dx][dy][value] = visited[dx][dy][dir] + 1
                            queue.append([[dx, dy], value])

                elif matrix[dx][dy] == 'C':
                    visited[dx][dy][dir] = visited[x][y][dir]
                    ret.append(visited[dx][dy][dir])
    print(min(ret) - 1)
bfs()