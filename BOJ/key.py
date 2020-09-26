import sys
from collections import deque

T = int(sys.stdin.readline())
a_to_A = ord('A') - ord('a')

dir_x = [-1, 0, 0, 1]
dir_y = [0, -1, 1, 0]

def bfs():
    count = 0
    visited = [[False for _ in range(W)] for _ in range(H)]
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx, dy = x + dir_x[i], y + dir_y[i]
            if 0 <= dx < H and 0 <= dy < W:
                if not visited[dx][dy]:
                    value = matrix[dx][dy]
                    if value == '.':
                        visited[dx][dy] = True
                        queue.append([dx, dy])

                    elif 'A' <= value <= 'Z':
                        if value in keys:
                            matrix[dx][dy] = '.'
                            visited[dx][dy] = True
                            queue.append([dx, dy])

                    elif 'a' <= value <= 'z':
                        big_alpha = chr(ord(value) + a_to_A)
                        if big_alpha not in keys:
                            queue = deque()
                            visited = [[False for _ in range(W)] for _ in range(H)]
                        matrix[dx][dy] = '.'
                        visited[dx][dy] = True
                        keys.add(big_alpha)
                        queue.append([dx, dy])

                    elif value == '$':
                        matrix[dx][dy] = '.'
                        visited[dx][dy] = True
                        queue.append([dx, dy])
                        count += 1
    print(count)


for _ in range(T):
    keys = set()
    h, w = map(int, sys.stdin.readline().split())
    H, W = h + 2, w + 2
    matrix = [['.' for _ in range(W)] for _ in range(H)]
    for i in range(h):
        tmp = sys.stdin.readline().strip()
        for j in range(w):
            matrix[i + 1][j + 1] = tmp[j]
    key_input = sys.stdin.readline().strip()

    for i in range(len(key_input)):
        keys.add(chr(ord(key_input[i]) + a_to_A))
    bfs()