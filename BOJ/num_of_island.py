import sys

direction = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]

def dfs(matrix, root):
    stack = []
    stack.append(root)

    while stack:
        a, b = stack.pop()
        visited[a][b] = True
        for value in direction:
            dx, dy = a + value[0], b + value[1]
            if 0 <= dx < h and 0 <= dy < w:
                if not visited[dx][dy]:
                    stack.append([dx, dy])
    return 1

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    matrix = [[0 for _ in range(w)] for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    for i in range(h):
        tmp = list(map(int, sys.stdin.readline().split()))
        for j in range(w):
            matrix[i][j] = tmp[j]
            if tmp[j] == 0:
                visited[i][j] = True
    count = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                count += dfs(matrix, [i, j])
    print(count)