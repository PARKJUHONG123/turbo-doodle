import sys

N, M = map(int, sys.stdin.readline().split())

matrix = [['.' for _ in range(M)] for _ in range(N)]
star_index = list()
cross_info = list()

def find_cross(star):
    x, y, length = star[0], star[1], 1
    while True:
        for i in range(4):
            if i == 0:
                dx, dy = x - length, y
            elif i == 1:
                dx, dy = x + length, y
            elif i == 2:
                dx, dy = x, y - length
            else:
                dx, dy = x, y + length
            if 0 <= dx < N and 0 <= dy < M:
                if (dx, dy) not in star_index:
                    return length - 1
            else:
                return length - 1
        length += 1

for i in range(N):
    temp = sys.stdin.readline().strip()
    for j in range(M):
        matrix[i][j] = temp[j]
        if matrix[i][j] == '*':
            star_index.append((i, j))

for star in star_index:
    cross = find_cross(star)
    if cross != 0:
        cross_info.append([star[0], star[1], cross])

for cross in cross_info:
    x, y, input_length = cross
    matrix[x][y] = '.'
    for length in range(1, input_length + 1):
        for i in range(4):
            if i == 0:
                dx, dy = x - length, y
            elif i == 1:
                dx, dy = x + length, y
            elif i == 2:
                dx, dy = x, y - length
            else:
                dx, dy = x, y + length
            matrix[dx][dy] = '.'

for value in matrix:
    if '*' in value:
        print(-1)
        exit()
print(len(cross_info))
for cross in cross_info:
    print(cross[0] + 1, cross[1] + 1, cross[2])