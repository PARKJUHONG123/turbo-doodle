import sys
from collections import deque

dir_x = [1, -1, 1, -1, 2, 2, -2, -2]
dir_y = [2, 2, -2, -2, 1, -1, 1, -1]

N = int(sys.stdin.readline().strip())

for _ in range(N):
    I = int(sys.stdin.readline().strip())
    knight = list(map(int, sys.stdin.readline().split()))
    target = list(map(int, sys.stdin.readline().split()))

    queue = deque()
    queue.append([knight, 0])
    visited = [[False for _ in range(I)] for _ in range(I)]
    visited[knight[0]][knight[1]] = True

    while queue:
        pos, count = queue.popleft()
        x, y = pos[0], pos[1]
        if target[0] == x and target[1] == y:
            print(count)
            break

        for i in range(8):
            dx, dy = x + dir_x[i], y + dir_y[i]
            if 0 <= dx < I and 0 <= dy < I:
                if not visited[dx][dy]:
                    queue.append([[dx, dy], count + 1])
                    visited[dx][dy] = True


