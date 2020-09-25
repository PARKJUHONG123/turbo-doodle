import sys
from collections import deque

dir = [[1, 0], [0, 1], [0, -1], [-1, 0]]
M, N = map(int, sys.stdin.readline().split())
matrix = [[0 for _ in range(M)] for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]

def bfs(root):
    queue = deque()
    queue.append(root)

    while queue:
        a, b = queue.popleft()
        for value in dir:
            dx, dy = a + value[0], b + value[1]
            if 0 <= dx < N and 0 <= dy < M:
                if visited[dx][dy] == -1:
                    if matrix[dx][dy] == 1:
                        queue.append([dx, dy])
                        visited[dx][dy] = visited[a][b] + 1
                    else:
                        queue.appendleft([dx, dy])
                        visited[dx][dy] = visited[a][b]

for i in range(N):
    tmp = sys.stdin.readline()
    for j in range(M):
        matrix[i][j] = int(tmp[j])
visited[0][0] = 0
bfs([0, 0])
print(visited[-1][-1])
