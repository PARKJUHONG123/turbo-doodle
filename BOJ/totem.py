import sys
N = int(sys.stdin.readline())
DN = N * 2
length = (DN * N - N) // 2
tiles = [[-1 for _ in range(DN)] for _ in range(N)]

for i in range(N):
    if i % 2 == 1:
        tiles[i][0], tiles[i][-1] = 0, 0

width, height = 0, 0
for i in range(length + 1):
    a, b = map(int, sys.stdin.readline().split())

    while True:
        if tiles[height][width] != -1:
            width += 1
            if width == DN:
                width = 0
                height += 1
        else:
            tiles[height][width] = a
            break

    while True:
        if tiles[height][width] != -1:
            width += 1
            if width == DN:
                width = 0
                height += 1
        else:
            tiles[height][width] = b
            break

def bfs