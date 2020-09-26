import sys
from collections import deque

bottles = list(map(int, sys.stdin.readline().split()))

def pour(bottle, first, second, first_index, second_index):
    ret = []
    if bottle == 0:
        ret.append([bottle, first, second])
        return ret
    if bottle + first > bottles[first_index]:
        bottle -= bottles[first_index] - first
        first = bottles[first_index]
    else:
        first += bottle
        bottle = 0
    ret.append([bottle, first, second])

    if bottle == 0:
        return ret
    if bottle + second > bottles[second_index]:
        bottle -= bottles[second_index] - second
        second = bottles[second_index]
    else:
        second += bottle
        bottle = 0
    ret.append([bottle, first, second])
    return ret

def bfs():
    queue = deque()
    queue.append([0, 0, bottles[2]])
    visited = [[False for _ in range(201)] for _ in range(201)]

    while queue:
        a, b, c = queue.popleft()
        if not visited[a][c]:
            visited[a][c] = True
            for value in pour(a, b, c, 1, 2):
                queue.append(value)
            for value in pour(a, c, b, 2, 1):
                queue.append([value[0], value[2], value[1]])

            for value in pour(b, a, c, 0, 2):
                queue.append([value[1], value[0], value[2]])
            for value in pour(b, c, a, 2, 0):
                queue.append([value[2], value[0], value[1]])

            for value in pour(c, a, b, 0, 1):
                queue.append([value[1], value[2], value[0]])
            for value in pour(c, b, a, 1, 0):
                queue.append([value[2], value[1], value[0]])

    return visited[0][:bottles[2] + 1]

ret, arr = bfs(), []
for i in range(bottles[2] + 1):
    if ret[i]:
        arr.append(i)
print(*arr)
