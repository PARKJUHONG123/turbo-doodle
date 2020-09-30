import sys
from collections import deque
T = int(sys.stdin.readline())

dir_x = [-1, 0, 0, 1]
dir_y = [0, -1, 1, 0]

def bfs(a, b):
    visited = [[-1 for _ in range(W)] for _ in range(H)]
    queue = deque()
    queue.append([a, b])
    visited[a][b] = 0
    while queue:
        x, y= queue.popleft()
        for i in range(4):
            dx, dy = x + dir_x[i], y + dir_y[i]
            if 0 <= dx < H and 0 <= dy < W:
                if visited[dx][dy] == -1:
                    if matrix[dx][dy] == '#':
                        visited[dx][dy] = visited[x][y] + 1
                        queue.append([dx, dy])
                    elif matrix[dx][dy] == '.':
                        visited[dx][dy] = visited[x][y]
                        queue.appendleft([dx, dy])
    return visited

for _ in range(T):
    h, w = map(int, sys.stdin.readline().split())
    H, W = h + 2, w + 2

    matrix = [['.' for _ in range(W)] for _ in range(H)]
    prisoners = []
    for i in range(h):
        tmp = sys.stdin.readline()
        for j in range(w):
            if tmp[j] == '$':
                prisoners.append([i + 1, j + 1])
                matrix[i + 1][j + 1] = '.'
            else:
                matrix[i + 1][j + 1] = tmp[j]

    a = (bfs(0, 0))
    b = (bfs(prisoners[0][0], prisoners[0][1]))
    c = (bfs(prisoners[1][0], prisoners[1][1]))

    min_count = 987654321
    for i in range(H):
        for j in range(W):
            if a[i][j] != -1 and b[i][j] != -1 and c[i][j] != -1:
                count = a[i][j] + b[i][j] + c[i][j]
                if matrix[i][j] == '#':
                    count -= 2
                min_count = min(min_count, count)
    print(min_count)

