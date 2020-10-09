import sys
from collections import deque
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

matrix = [[] for _ in range(N)]
for i in range(N):
    matrix[i] = list(map(int, sys.stdin.readline().split()))

empty_list = []
virus_list = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            empty_list.append((i, j))
        elif matrix[i][j] == 2:
            virus_list.append((i, j))
three_choose_list = combinations(empty_list, 3)

dir_x = [-1, 0, 0, 1]
dir_y = [0, -1, 1, 0]

def bfs(three_element):
    for value in three_element:
        matrix[value[0]][value[1]] = 1
    queue = deque()
    count = 0

    for value in virus_list:
        queue.append(value)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx, dy = x + dir_x[i], y + dir_y[i]
            if 0 <= dx < N and 0 <= dy < M:
                if matrix[dx][dy] == 0:
                    matrix[dx][dy] = 3
                    queue.append((dx, dy))
    for value in matrix:
        count += value.count(0)

    for value in three_element:
        matrix[value[0]][value[1]] = 0

    for i in range(N):
        for j in range(M):
            matrix[i][j] = (0 if matrix[i][j] == 3 else matrix[i][j])
    return count

max_count = 0
for value in three_choose_list:
    max_count = max(max_count, bfs(value))
print(max_count)
