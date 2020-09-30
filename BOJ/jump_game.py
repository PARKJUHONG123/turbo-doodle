import sys
from collections import deque
N, k = map(int, sys.stdin.readline().split())

lines = ["" for _ in range(2)]
for i in range(2):
    lines[i] = sys.stdin.readline().strip()
visited = [[False for _ in range(N)] for _ in range(2)]

def bfs():
    queue = deque()
    queue.append([[0, 0], 0])
    visited[0][0] = True

    while queue:
        [x, y], height = queue.popleft()
        dx, dy = abs(x - 1), y + k
        if 0 <= dy < N:
            if not visited[dx][dy] and height < dy and lines[dx][dy] == '1':
                queue.append([[dx, dy], height + 1])
                visited[dx][dy] = True
        elif dy >= N:
            print(1)
            exit()

        dx, dy = x, y - 1
        if 0 <= dy < N:
            if not visited[dx][dy] and height < dy and lines[dx][dy] == '1':
                queue.append([[dx, dy], height + 1])
                visited[dx][dy] = True
        elif dy >= N:
            print(1)
            exit()

        dx, dy = x, y + 1
        if 0 <= dy < N:
            if not visited[dx][dy] and height < dy and lines[dx][dy] == '1':
                queue.append([[dx, dy], height + 1])
                visited[dx][dy] = True
        elif dy >= N:
            print(1)
            exit()
    print(0)
bfs()
