import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
matrix = [[[] for _ in range(M)] for _ in range(N)]

B, R = 0, 0
for i in range(N):
    tmp = sys.stdin.readline()
    for j in range(M):
        if tmp[j] == 'B':
            B = [i, j]
            matrix[i][j] = '.'
        elif tmp[j] == 'R':
            R = [i, j]
            matrix[i][j] = '.'
        else:
            matrix[i][j] = tmp[j]

def left(x, y):
    while True:
        dx, dy = x, y - 1
        if matrix[dx][dy] == '.':
            x, y = dx, dy
        elif matrix[dx][dy] == 'O':
            return [True, dx, dy]
        elif matrix[dx][dy] == '#':
            return [False, x, y]

def right(x, y):
    while True:
        dx, dy = x, y + 1
        if matrix[dx][dy] == '.':
            x, y = dx, dy
        elif matrix[dx][dy] == 'O':
            return [True, dx, dy]
        elif matrix[dx][dy] == '#':
            return [False, x, y]

def up(x, y):
    while True:
        dx, dy = x - 1, y
        if matrix[dx][dy] == '.':
            x, y = dx, dy
        elif matrix[dx][dy] == 'O':
            return [True, dx, dy]
        elif matrix[dx][dy] == '#':
            return [False, x, y]

def down(x, y):
    while True:
        dx, dy = x + 1, y
        if matrix[dx][dy] == '.':
            x, y = dx, dy
        elif matrix[dx][dy] == 'O':
            return [True, dx, dy]
        elif matrix[dx][dy] == '#':
            return [False, x, y]

def bfs():
    queue = deque()
    visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[B[0]][B[1]][R[0]][R[1]] = True
    queue.append([B[0], B[1], R[0], R[1], 1])

    while queue:
        bx, by, rx, ry, count = queue.popleft()
        for i in range(4):
            if i == 0:
                B_done, BX, BY = left(bx, by)
                R_done, RX, RY = left(rx, ry)
                if not (B_done and R_done):
                    if BX == RX and BY == RY:
                        if by < ry:
                            RY += 1
                        else:
                            BY += 1

            elif i == 1:
                B_done, BX, BY = right(bx, by)
                R_done, RX, RY = right(rx, ry)
                if not (B_done and R_done):
                    if BX == RX and BY == RY:
                        if by < ry:
                            BY -= 1
                        else:
                            RY -= 1

            elif i == 2:
                B_done, BX, BY = up(bx, by)
                R_done, RX, RY = up(rx, ry)
                if not (B_done and R_done):
                    if BX == RX and BY == RY:
                        if bx < rx:
                            RX += 1
                        else:
                            BX += 1

            else:
                B_done, BX, BY = down(bx, by)
                R_done, RX, RY = down(rx, ry)
                if not (B_done and R_done):
                    if BX == RX and BY == RY:
                        if bx < rx:
                            BX -= 1
                        else:
                            RX -= 1

            if not visited[BX][BY][RX][RY]:
                visited[BX][BY][RX][RY] = True
                if not B_done:
                    if R_done:
                        return count
                    else:
                        queue.append([BX, BY, RX, RY, count + 1])
    return -1

print(bfs())