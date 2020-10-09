import sys
import copy
N, M = map(int, sys.stdin.readline().split())
matrix = [[] for _ in range(N)]
for i in range(N):
    matrix[i] = list(map(int, sys.stdin.readline().split()))

visited = list()
cctv = list()
dir_x = [-1, 0, 1, 0]
dir_y = [0, 1, 0, -1]

def watch_one_dir(start_x, start_y, dir):
    x, y = start_x, start_y
    while True:
        dx, dy = x + dir_x[dir], y + dir_y[dir]
        if 0 <= dx < N and 0 <= dy < M:
            if matrix[dx][dy] != 6:
                if matrix[dx][dy] == 0:
                    matrix[dx][dy] = 7
            else:
                break
        else:
            break
        x, y = dx, dy

def count_zero():
    count = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                count += 1
    return count

for i in range(N):
    for j in range(M):
        if 1 <= matrix[i][j] <= 4:
            cctv.append((matrix[i][j], i, j))
            visited.append(-1)
        elif matrix[i][j] == 5:
            for k in range(4):
                watch_one_dir(i, j, k)

sample_matrix = copy.deepcopy(matrix)

length = len(visited)
min_count = 987654321
def brute(index):
    global min_count, matrix
    if index < length:
        for i in range(4):
            visited[index] = i
            brute(index + 1)

            for j in range(length):
                front = visited[j]
                cctv_type, start_x, start_y = cctv[j][0], cctv[j][1], cctv[j][2]
                if cctv_type == 1:
                    watch_one_dir(start_x, start_y, front)

                elif cctv_type == 2:
                    watch_one_dir(start_x, start_y, front)
                    back = (front + 2 if front < 2 else front - 2)
                    watch_one_dir(start_x, start_y, back)

                elif cctv_type == 3:
                    watch_one_dir(start_x, start_y, front)
                    right = (front + 1 if front < 3 else 0)
                    watch_one_dir(start_x, start_y, right)

                elif cctv_type == 4:
                    watch_one_dir(start_x, start_y, front)
                    back = (front + 2 if front < 2 else front - 2)
                    watch_one_dir(start_x, start_y, back)
                    right = (front + 1 if front < 3 else 0)
                    watch_one_dir(start_x, start_y, right)

            min_count = min(min_count, count_zero())
            matrix = copy.deepcopy(sample_matrix)

brute(0)

if min_count == 987654321:
    min_count = min(min_count, count_zero())
print(min_count)