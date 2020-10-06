import sys
from collections import deque

T = 4
gears = [[] for _ in range(T)]
for i in range(T):
    tmp = sys.stdin.readline().strip()
    for j in range(8):
        gears[i].append(int(tmp[j]))

clock_index = [[6, 2] for _ in range(T)]

def rotate_cw(index):
    clock_index[index][0] -= 1
    clock_index[index][1] -= 1

    if clock_index[index][0] == -1:
        clock_index[index][0] = 7
    elif clock_index[index][1] == -1:
        clock_index[index][1] = 7

def rotate_ccw(index):
    clock_index[index][0] += 1
    clock_index[index][1] += 1

    if clock_index[index][0] == 8:
        clock_index[index][0] = 0
    elif clock_index[index][1] == 8:
        clock_index[index][1] = 0

K = int(sys.stdin.readline().strip())

for _ in range(K):
    start_index, direction = map(int, sys.stdin.readline().split())
    start_index -= 1
    rotation_list = [0 for _ in range(T)]
    rotation_list[start_index] = direction

    for i in reversed(range(1, start_index + 1)): # 2, 1, 0
        if gears[i][clock_index[i][0]] != gears[i - 1][clock_index[i - 1][1]]:
            rotation_list[i - 1] = (1 if rotation_list[i] == -1 else -1)
        else:
            break

    for i in range(start_index, T - 1): # 2, 3
        if gears[i][clock_index[i][1]] != gears[i + 1][clock_index[i + 1][0]]:
            rotation_list[i + 1] = (1 if rotation_list[i] == -1 else -1)
        else:
            break

    for i in range(T):
        if rotation_list[i] == -1:
            rotate_ccw(i)
        elif rotation_list[i] == 1:
            rotate_cw(i)

answer = 0
for i in range(T):
    index = clock_index[i][1] - 2
    if index < 0:
        index += 8
    if gears[i][index] == 1:
        answer += pow(2, i)
print(answer)
