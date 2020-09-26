import sys
from collections import deque
T = int(sys.stdin.readline())

dir_x = [-1, 0, 0, 1]
dir_y = [0, -1, 1, 0]

def bfs(prisoner, visited):
    queue = deque()
    queue.append(prisoner)
    x, y = prisoner
    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx, dy = x + dir_x[i], y + dir_y[i]
            if 0 <= dx < h and 0 <= dy < w:
                if visited[dx][dy] == -1:
                    value = matrix[dx][dy]
                    if value == '$' or value == '.':
                        visited[dx][dy] = visited[x][y]
                        queue.append([dx, dy])
                    elif value == '#':
                        visited[dx][dy] = visited[x][y] + 1
                        queue.append([dx, dy])

for _ in range(T):
    h, w = map(int, sys.stdin.readline().split())
    matrix = [list(sys.stdin.readline().strip()) for _ in range(h)]
    prisoner = []
    visited_1 = [[-2 for _ in range(w)] for _ in range(h)]
    visited_2 = [[-2 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            value = matrix[i][j]
            if value == '$':
                prisoner.append([i, j])
                visited_1[i][j] = -1
                visited_2[i][j] = -1
            elif value == '.':
                visited_1[i][j] = -1
                visited_2[i][j] = -1
            elif value == '#':
                visited_1[i][j] = -1
                visited_2[i][j] = -1

    bfs(prisoner[0], visited_1)
    bfs(prisoner[1], visited_2)

    min_value = 987654321

    for value in visited_1:
        print(value)
    print("")
    for value in visited_2:
        print(value)
    print("")

    for i in range(h):
        j = 0
        value = visited_1[i][j] + visited_2[i][j]
        if value >= 0:
            min_value = min(min_value, value)
        j = w - 1
        value = visited_1[i][j] + visited_2[i][j]
        if value >= 0:
            min_value = min(min_value, value)

    for j in range(w):
        i = 0
        value = visited_1[i][j] + visited_2[i][j]
        if value >= 0:
            min_value = min(min_value, value)
        i = h - 1
        value = visited_1[i][j] + visited_2[i][j]
        if value >= 0:
            min_value = min(min_value, value)

    print(min_value // 2)