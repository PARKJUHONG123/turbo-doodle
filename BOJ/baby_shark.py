import sys
from collections import deque
N = int(sys.stdin.readline().strip())
matrix = [[] for _ in range(N)]

baby_shark_location = []
baby_shark_size = 2
eaten_fish = 0

for i in range(N):
    matrix[i] = list(map(int, sys.stdin.readline().split()))
    if 9 in matrix[i]:
        for j in range(N):
            if matrix[i][j] == 9:
                baby_shark_location = [i, j]
                matrix[i][j] = 0

def mom_call():
    for i in range(N):
        for j in range(N):
            if 0 < matrix[i][j] < baby_shark_size:
                return False
    return True

x_list = [0, -1, 1, 0]
y_list = [-1, 0, 0, 1]

total_time = 0

def eat(tx, ty, time):
    global eaten_fish, baby_shark_location, total_time, eaten_fish, baby_shark_size
    matrix[tx][ty] = 0
    eaten_fish += 1
    baby_shark_location = [tx, ty]
    if baby_shark_size == eaten_fish:
        eaten_fish = 0
        baby_shark_size += 1
    total_time += time

def choose_fish(eat_able, last_time):
    temp_dict = dict()
    for element in eat_able:
        if element[0] in temp_dict:
            temp_dict[element[0]].append(element[1])
        else:
            temp_dict[element[0]] = [element[1]]

    height = min(temp_dict.keys())
    width = min(temp_dict[height])
    eat(height, width, last_time)

def bfs():
    queue = deque()
    x, y = baby_shark_location
    queue.append([x, y, 0])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[x][y] = True
    eat_able = list()
    last_time = -1

    while queue:
        tx, ty, time = queue.popleft()
        if time >= N * N:
            return False

        if last_time == time:
            if 0 < matrix[tx][ty] < baby_shark_size:
                eat_able.append([tx, ty])
        else:
            if eat_able:
                choose_fish(eat_able, last_time)
                return True

            else:
                last_time = time
                if 0 < matrix[tx][ty] < baby_shark_size:
                    eat_able.append([tx, ty])

        for i in range(4):
            dx, dy = tx + x_list[i], ty + y_list[i]
            if 0 <= dx < N and 0 <= dy < N:
                if not visited[dx][dy]:
                    if matrix[dx][dy] <= baby_shark_size:
                        visited[dx][dy] = True
                        queue.append([dx, dy, time + 1])
    if eat_able:
        choose_fish(eat_able, last_time)
        return True

def brute():
    while True:
        if mom_call():
            break
        if not bfs():
            break
    print(total_time)

brute()