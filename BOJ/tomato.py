import sys
from collections import deque

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

M, N = list(map(int, sys.stdin.readline().split()))
matrix = [[0 for _ in range(M)] for _ in range(N)]

ripen = True
start_list = []
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        matrix[i][j] = tmp[j]
        if matrix[i][j] == 1:
            start_list.append([i, j])
    if 0 in matrix[i]:
        ripen = False
if ripen:
    print(0)
    exit()

max_count = -1
def bfs():
    global max_count
    queue = deque()
    count = 1
    for value in start_list:
        queue.append([value, count])

    while queue:
        tmp = queue.popleft()
        tx, ty = tmp[0][0], tmp[0][1]
        count = tmp[1]
        max_count = max(max_count, count)

        for value in direction:
            dx, dy = tx + value[0], ty + value[1]
            if 0 <= dx < N and 0 <= dy < M:
                if matrix[dx][dy] == 0:
                    matrix[dx][dy] = count + 1
                    queue.append([[dx, dy], count + 1])
bfs()

token = True
for i in range(N):
    if 0 in matrix[i]:
        token = False
        break

if token:
    print(max_count - 1)
else:
    print(-1)
