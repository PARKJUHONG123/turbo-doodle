T = int(input())

dir_x = [-1, 0, 1, 0]
dir_y = [0, -1, 0, 1]

def brute(index, connected, outer_count):
    if outer_count != 0:
        min_connect[connected] = min(outer_count, min_connect[connected])
    if index == length:
        return

    cx, cy = core_list[index]
    for i in range(4):
        x, y, count = cx, cy, 0
        token = False
        while True:
            dx, dy = dir_x[i] + x, dir_y[i] + y
            if matrix[dx][dy] == 0:
                count += 1
                if dx == 0 or dx == N - 1 or dy == 0 or dy == N - 1:
                    token = True
                    break
                x, y = dx, dy
            else:
                break

        if token:
            vx, vy = cx, cy
            for j in range(1, count + 1):
                vx, vy = cx + dir_x[i] * j, cy + dir_y[i] * j
                matrix[vx][vy] = 2

            brute(index + 1, connected + 1, outer_count + count)
            rx, ry, ri = vx, vy, (i - 2 if i >= 2 else i + 2)
            for j in range(count):
                vx, vy = rx + dir_x[ri] * j, ry + dir_y[ri] * j
                matrix[vx][vy] = 0
    brute(index + 1, connected, outer_count)

for index in range(T):
    max_num = 987654321
    N = int(input())
    min_connect = [max_num for _ in range(N + 1)]
    matrix = [[] for _ in range(N)]

    core_list = []
    for i in range(N):
        matrix[i] = list(map(int, input().split()))
        for j in range(N):
            if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                continue
            if matrix[i][j] == 1:
                core_list.append([i, j])
    length = len(core_list)
    brute(0, 0, 0)
    best_answer = 0
    for value in reversed(min_connect):
        if value != max_num:
            best_answer = value
            break

    print("#" + str(index + 1) + " " + str(best_answer))