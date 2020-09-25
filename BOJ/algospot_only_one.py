import sys
from collections import deque

dir = [[1, 0], [0, 1], [0, -1], [-1, 0]]
N, M = map(int, sys.stdin.readline().split())
matrix = [[0 for _ in range(M)] for _ in range(N)]
visited = [[[-1 for _ in range(2)] for _ in range(M)] for _ in range(N)]

def bfs():
    queue = deque()
    queue.append([0, 0, False])

    while queue:
        a, b, broken = queue.popleft()

        for value in dir:
            dx, dy = a + value[0], b + value[1]
            if 0 <= dx < N and 0 <= dy < M:
                if broken:
                    if matrix[dx][dy] == 0 and visited[dx][dy][1] == -1:
                        visited[dx][dy][1] = visited[a][b][1] + 1
                        queue.append([dx, dy, broken])
                else:
                    if matrix[dx][dy] == 0 and visited[dx][dy][0] == -1:
                        visited[dx][dy][0] = visited[a][b][0] + 1
                        queue.append([dx, dy, broken])

                    elif matrix[dx][dy] == 1 and visited[dx][dy][1] == -1:
                        visited[dx][dy][1] = visited[a][b][0] + 1
                        queue.append([dx, dy, True])


for i in range(N):
    tmp = sys.stdin.readline()
    for j in range(M):
        matrix[i][j] = int(tmp[j])
visited[0][0][0] = 0
bfs()

none_break = visited[-1][-1][0]
one_break = visited[-1][-1][1]

if none_break == -1 and one_break == -1:
    print(-1)
else:
    if none_break == -1:
        print(one_break + 1)
    elif one_break == -1:
        print(none_break + 1)
    else:
        print(min(one_break, none_break) + 1)