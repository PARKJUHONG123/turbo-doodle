import sys

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
matrix = [list() for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    matrix[i] = list(map(int, sys.stdin.readline().split()))

visited[r][c] = True

dir_x = [-1, 0, 1, 0]
dir_y = [0, 1, 0, -1]

def dfs(a, b, direction):
    stack = list()
    stack.append([[a, b], direction])
    visited[a][b] = True

    while stack:
        [x, y], i = stack.pop()

        inner_count = 0
        for j in range(4):
            tx, ty = x + dir_x[j], y + dir_y[j]
            if visited[tx][ty] or matrix[tx][ty] == 1:
                inner_count += 1

        if inner_count == 4:
            back = (i + 2 if i + 2 < 4 else i - 2)
            bx, by = x + dir_x[back], y + dir_y[back]
            if matrix[bx][by] == 0:
                stack.append([[bx, by], i])
                continue
            else:
                return

        left_i = (i - 1 if i != 0 else 3)
        dx, dy = x + dir_x[left_i], y + dir_y[left_i]
        if matrix[dx][dy] == 0:
            if not visited[dx][dy]:
                visited[dx][dy] = True
                stack.append([[dx, dy], left_i])
            else:
                stack.append([[x, y], left_i])
        else:
            stack.append([[x, y], left_i])

dfs(r, c, d)
count = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0 and visited[i][j]:
            count += 1
print(count)