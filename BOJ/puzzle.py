import sys
from collections import deque
puzzle = 0

height = pow(10, 8)
zero_index = -1
for j in range(3):
    tmp = list(map(int, sys.stdin.readline().split()))
    for i in range(3):
        if tmp[i] == 0:
            zero_index = 8 - (j * 3 + i)
        puzzle += height * tmp[i]
        height //= 10

def bfs():
    visited = dict()
    queue = deque()
    queue.append([puzzle, zero_index, 0])
    visited[puzzle] = True

    while queue:
        num, zero, count = queue.popleft()
        if num == 123456780:
            print(count)
            exit()

        if zero + 1 <= 8 and zero != 5 and zero != 2:
            tmp = (num // pow(10, zero + 1)) % 10
            value = num + tmp * pow(10, zero) - tmp * pow(10, zero + 1)
            if value not in visited:
                visited[value] = True
                queue.append([value, zero + 1, count + 1])

        if zero - 1 >= 0 and zero != 6 and zero != 3:
            tmp = (num // pow(10, zero - 1)) % 10
            value = num + tmp * pow(10, zero) - tmp * pow(10, zero - 1)
            if value not in visited:
                visited[value] = True
                queue.append([value, zero - 1, count + 1])

        if zero - 3 >= 0:
            tmp = (num // pow(10, zero - 3)) % 10
            value = num + tmp * pow(10, zero) - tmp * pow(10, zero - 3)
            if value not in visited:
                visited[value] = True
                queue.append([value, zero - 3, count + 1])

        if zero + 3 <= 8:
            tmp = (num // pow(10, zero + 3)) % 10
            value = num + tmp * pow(10, zero) - tmp * pow(10, zero + 3)
            if value not in visited:
                visited[value] = True
                queue.append([value, zero + 3, count + 1])
    print(-1)
    exit()
bfs()