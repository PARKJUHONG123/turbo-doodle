import sys

C, P = map(int, sys.stdin.readline().split())

heights = list(map(int, sys.stdin.readline().split()))
max_height = max(heights) + 6
matrix = [[False for _ in range(max_height)] for _ in range(C)]

for i in range(C):
    for j in range(heights[i] + 1):
        matrix[i][j] = True

def built_count(start_x, start_y, end_x, end_y):
    ret = 0
    if 0 <= start_x < C and 0 <= start_y < max_height and 0 <= end_x < C and 0 <= end_y < max_height:
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if matrix[x][y]:
                    ret += 1
    return ret

count = 0
def brute(x, y):
    global count
    if P == 1:
        max_dx, max_dy = x + 3, y + 1
        if built_count(x, y, max_dx, max_dy) == 4:
            if matrix[x][y] and matrix[x + 1][y] and matrix[x + 2][y] and matrix[x + 3][y]:
                count += 1

        max_dx, max_dy = x, y + 5
        if built_count(x, y, max_dx, max_dy) == 1:
            if matrix[x][y]:
                count += 1

    elif P == 2:
        max_dx, max_dy = x + 1, y + 2
        if built_count(x, y, max_dx, max_dy) == 2:
            if matrix[x][y] and matrix[x + 1][y]:
                count += 1

    elif P == 3:
        max_dx, max_dy = x + 1, y + 3
        if built_count(x, y, max_dx, max_dy) == 3:
            if matrix[x][y] and matrix[x + 1][y] and matrix[x][y + 1]:
                count += 1
        max_dx, max_dy = x + 2, y + 2
        if built_count(x, y, max_dx, max_dy) == 4:
            if matrix[x][y] and matrix[x + 1][y] and matrix[x + 2][y] and matrix[x + 2][y + 1]:
                count += 1

    elif P == 4:
        max_dx, max_dy = x + 1, y + 3
        if built_count(x, y, max_dx, max_dy) == 3:
            if matrix[x][y] and matrix[x + 1][y] and matrix[x + 1][y + 1]:
                count += 1
        max_dx, max_dy = x + 2, y + 2
        if built_count(x, y, max_dx, max_dy) == 4:
            if matrix[x][y] and matrix[x][y + 1] and matrix[x + 1][y] and matrix[x + 2][y]:
                count += 1

    elif P == 5:
        max_dx, max_dy = x + 2, y + 2
        m = built_count(x, y, max_dx, max_dy)
        if m == 3:
            if matrix[x][y] and matrix[x + 1][y] and matrix[x + 2][y]:
                count += 1
        elif m == 5:
            if matrix[x][y] and matrix[x + 1][y] and matrix[x + 2][y] and matrix[x][y + 1] and matrix[x + 2][y + 1]:
                count += 1

        max_dx, max_dy = x + 1, y + 3
        if built_count(x, y, max_dx, max_dy) == 3:
            if matrix[x][y] and matrix[x + 1][y]:
                if matrix[x][y + 1]:
                    count += 1
                elif matrix[x + 1][y + 1]:
                    count += 1

    elif P == 6:
        max_dx, max_dy = x + 1, y + 3
        h = built_count(x, y, max_dx, max_dy)
        if h == 4:
            if matrix[x][y] and matrix[x][y + 1] and matrix[x][y + 2] and matrix[x + 1][y]:
                count += 1
        elif h == 2:
            if matrix[x][y] and matrix[x + 1][y]:
                count += 1

        max_dx, max_dy = x + 2, y + 2
        w = built_count(x, y, max_dx, max_dy)
        if w == 5:
            if matrix[x][y] and matrix[x + 1][y] and matrix[x + 2][y] and matrix[x + 1][y + 1] and matrix[x + 2][y + 1]:
                count += 1
        elif w == 3:
            if matrix[x][y] and matrix[x + 1][y] and matrix[x + 2][y]:
                count += 1

    elif P == 7:
        max_dx, max_dy = x + 1, y + 3
        h = built_count(x, y, max_dx, max_dy)
        if h == 4:
            if matrix[x][y] and matrix[x + 1][y + 1] and matrix[x + 1][y + 2] and matrix[x + 1][y]:
                count += 1

        elif h == 2:
            if matrix[x][y] and matrix[x + 1][y]:
                count += 1

        max_dx, max_dy = x + 2, y + 2
        w = built_count(x, y, max_dx, max_dy)
        if w == 5:
            if matrix[x][y] and matrix[x + 1][y] and matrix[x + 2][y] and matrix[x + 1][y + 1] and matrix[x][y + 1]:
                count += 1

        if w == 3:
            if matrix[x][y] and matrix[x + 1][y] and matrix[x + 2][y]:
                count += 1

for i in range(C):
    for j in range(max_height):
        brute(i, j)
print(count)