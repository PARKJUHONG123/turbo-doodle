import sys

s, n = sys.stdin.readline().split()
s = int(s)
n_length = len(n)
width, height = s + 2, 2 * s + 3
total_width = width * n_length
matrix = [[] for _ in range(height)]

for index in range(n_length):
    number = int(n[index])

    inner_matrix = [[' ' for _ in range(width)] for _ in range(height)]

    mid_height = height // 2
    end_width, end_height = width - 1, height - 1

    for i in range(height):
        for j in range(width):
            if j == 0 or j == end_width:
                inner_matrix[i][j] = '|'
            if i == 0 or i == mid_height or i == end_height:
                inner_matrix[i][j] = '-'
    inner_matrix[0][0] = inner_matrix[0][end_width] = inner_matrix[mid_height][0] = inner_matrix[mid_height][end_width] = inner_matrix[end_height][0] = inner_matrix[end_height][end_width] = ' '

    if number == 0:
        for j in range(width):
            inner_matrix[mid_height][j] = ' '

    elif number == 1:
        for j in range(width):
            inner_matrix[0][j] = ' '
            inner_matrix[mid_height][j] = ' '
            inner_matrix[end_height][j] = ' '
        for j in range(height):
            inner_matrix[j][0] = ' '

    elif number == 2:
        for j in range(mid_height):
            inner_matrix[j][0] = ' '
        for j in range(mid_height, height):
            inner_matrix[j][end_width] = ' '

    elif number == 3:
        for j in range(height):
            inner_matrix[j][0] = ' '

    elif number == 4:
        for j in range(width):
            inner_matrix[0][j] = ' '
            inner_matrix[end_height][j] = ' '
        for j in range(mid_height, height):
            inner_matrix[j][0] = ' '

    elif number == 5:
        for j in range(mid_height):
            inner_matrix[j][end_width] = ' '
        for j in range(mid_height, height):
            inner_matrix[j][0] = ' '

    elif number == 6:
        for j in range(mid_height):
            inner_matrix[j][end_width] = ' '

    elif number == 7:
        for j in range(height):
            inner_matrix[j][0] = ' '
        for j in range(width):
            inner_matrix[mid_height][j] = ' '
            inner_matrix[end_height][j] = ' '

    elif number == 8:
        pass

    elif number == 9:
        for j in range(mid_height, height):
            inner_matrix[j][0] = ' '

    for i in range(height):
        matrix[i].extend(inner_matrix[i])
        matrix[i].append(' ')

for value in matrix:
    for element in value:
        print(element, end = '')
    print("")

