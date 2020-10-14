import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
N, M = N + 2, M + 2

dir_x = [-1, 0, 0, 1]
dir_y = [0, -1, 1, 0]

matrix = [['@' for _ in range(M)] for _ in range(N)]
coins = []

for i in range(1, N - 1):
    temp = sys.stdin.readline()
    for j in range(1, M - 1):
        if temp[j - 1] == 'o':
            coins.append((i, j))
            matrix[i][j] = '.'
        else:
            matrix[i][j] = temp[j - 1]


def bfs():
    queue = deque()
    visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
    a, b = coins[0]
    c, d = coins[1]
    visited[a][b][c][d] = True
    queue.append([a, b, c, d, 1])

    while queue:
        ax, ay, bx, by, count = queue.popleft()
        if count <= 10:
            for i in range(4):
                cx, dx = ax + dir_x[i], bx + dir_x[i]
                cy, dy = ay + dir_y[i], by + dir_y[i]
                if not visited[cx][cy][dx][dy]:
                    visited[cx][cy][dx][dy] = True
                    C, D = matrix[cx][cy], matrix[dx][dy]

                    if C == '@':
                        if D == '@':
                            pass
                        elif D == '.':
                            return count
                        elif D == '#':
                            return count

                    elif C == '.':
                        if D == '@':
                            return count

                        elif D == '.':
                            queue.append([cx, cy, dx, dy, count + 1])

                        elif D == '#':
                            queue.append([cx, cy, bx, by, count + 1])

                    elif C == '#':
                        if D == '@':
                            return count

                        elif D == '.':
                            queue.append([ax, ay, dx, dy, count + 1])

                        elif D == '#':
                            queue.append([ax, ay, bx, by, count + 1])
    return -1

print(bfs())
