import sys
def regular_triangle(x, y):
    total_sum, max_sum = 0, 0
    for i in range(x, height):
        end_point = y + 2 * (i - x) + 1
        if end_point > len(matrix[i]):
            break
        for j in range(y, end_point):
            total_sum += matrix[i][j]
        max_sum = max(max_sum, total_sum)
    return max_sum

def opposite_triangle(x, y):
    total_sum, max_sum = 0, 0
    count = 0
    for i in reversed(range(x + 1)):
        start_point = y - (2 * count + 1) + 1
        if start_point < 0 or y >= len(matrix[i]):
            break
        for j in range(start_point, y + 1):
            total_sum += matrix[i][j]
        max_sum = max(max_sum, total_sum)
        count += 1
    return max_sum

point_list = []
while True:
    tmp = list(map(int, sys.stdin.readline().split()))
    height = tmp[0]
    if height == 0:
        break
    matrix = [[] for _ in range(height)]
    start_index = 1
    for i in range(tmp[0]):
        end_index = start_index + (2 * i + 1)
        inner_list = tmp[start_index : end_index]
        matrix[i] = inner_list
        start_index = end_index

    # regular_triangle
    max_total = 0
    for i in range(height):
        for j in range(0, 2 * i + 1, 2):
            max_total = max(max_total, regular_triangle(i, j))
    for i in range(height):
        for j in range(1, len(matrix[i]), 2):
            max_total = max(max_total, opposite_triangle(i, j))
    point_list.append(max_total)

for i in range(len(point_list)):
    print(str(i + 1) + ". " + str(point_list[i]))
