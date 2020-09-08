#BFS 를 사용하여 조건에 맞게 설계하는 것이 포인트

import sys
from collections import deque

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
MN = sys.stdin.readline().split()
N = int(MN[0])
M = int(MN[1])
visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
arr = [["#" for _ in range(M)] for _ in range(N)]

for i in range(N):
    tmp = sys.stdin.readline()
    for j in range(M):
        arr[i][j] = tmp[j]
        if tmp[j] == 'R':
            rx, ry = i, j
        elif tmp[j] == 'B':
            bx, by = i, j

def move(x, y, dx, dy):
    count = 0
    while arr[x + dx][y + dy] != '#' and arr[x][y] != 'O':
        x, y, count = x + dx, y + dy, count + 1
    return x, y, count

def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append((rx, ry, bx, by, 1, -1))
    visited[rx][ry][bx][by] = True

    while queue:
        rx, ry, bx, by, depth, before_dir = queue.popleft()
        if depth > 10:
            break

        for i in range(4):
            if i != before_dir:
                nrx, nry, rcount = move(rx, ry, dx[i], dy[i])
                nbx, nby, bcount = move(bx, by, dx[i], dy[i])

                if arr[nbx][nby] == 'O':
                    continue
                if arr[nrx][nry] == 'O':
                    print(depth)
                    return

                if (nrx, nry) == (nbx, nby):
                    if rcount < bcount:
                        nbx, nby = nbx - dx[i], nby - dy[i]
                    else:
                        nrx, nry = nrx - dx[i], nry - dy[i]

                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, depth + 1, i))
    print(-1)
    return

bfs(rx, ry, bx, by)