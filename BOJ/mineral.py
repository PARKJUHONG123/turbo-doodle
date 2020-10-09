import sys

dir_x = [-1, 0, 0, 1]
dir_y = [0, -1, 1, 0]

R, C = map(int, sys.stdin.readline().split())
matrix = [[] for _ in range(R)]
for i in range(R):
    row = [False for _ in range(C)]
    tmp = sys.stdin.readline()
    for j in range(C):
        row[j] = (False if tmp[j] == '.' else True)
    matrix[i] = row

def dfs(matrix, height, width):
    stack = [[] for _ in range(4)]
    visited = [[] for _ in range(4)]
    fall = [True for _ in range(4)]
    for i in range(4):
        hx, hy = height + dir_x[i], width + dir_y[i]
        if 0 <= hx < R and 0 <= hy < C:
            if matrix[hx][hy]:
                stack[i].append([hx, hy])
                visited[i].append([hx, hy])

    for index in range(4):
        while stack[index]:
            rh, rw = stack[index].pop()
            for dir in range(4):
                dh, dw = rh + dir_x[dir], rw + dir_y[dir]
                if 0 <= dh < R and 0 <= dw < C:
                    if matrix[dh][dw] and [dh, dw] not in visited[index]:
                        if dh == R - 1:
                            visited[index].append([dh, dw])
                        else:
                            stack[index].append([dh, dw])
                            visited[index].append([dh, dw])
        if visited[index]:
            for value in visited[index]:
                if value[0] == R - 1:
                    fall[index] = False
                    break
        else:
            fall[index] = False
    for i in range(4):
        if fall[i]:
            visited[i].sort(reverse = True)
            max_height = -1
            max_list = list()
            for value in visited[i]:
                if max_height < value[0]:
                    max_height = value[0]
                    max_list.append(value)
                elif max_height == value[0]:
                    max_list.append(value)
                else:
                    break

            token = False
            for count in range(1, R):
                for value in max_list:
                    if value[0] + count >= R:
                        token = True
                        break
                    if matrix[value[0] + count][value[1]]:
                        token = True
                        break
                if token:
                    count -= 1
                    break
            for value in visited[i]:
                matrix[value[0]][value[1]] = False
                matrix[value[0] + count][value[1]] = True

N = int(sys.stdin.readline())
H = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    height = R - H[i]
    if i % 2 == 0: # left
        for w in range(C):
            if matrix[height][w]:
                matrix[height][w] = False
                break

    else: # right
        for w in reversed(range(C)):
            if matrix[height][w]:
                matrix[height][w] = False
                break

    dfs(matrix, height, w)


for i in range(R):
    for element in matrix[i]:
        if element == False:
            print(".", end = "")
        else:
            print("x", end = "")
    print("")
