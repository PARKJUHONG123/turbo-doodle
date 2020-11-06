import sys
from collections import deque
N = int(sys.stdin.readline().strip())
min_papers, zero_papers, plus_papers = 0, 0, 0
matrix = [[] for _ in range(N)]

def configure(x, y, length):
    min_configure, zero_configure, plus_configure = False, False, False
    for i in range(x, x + length):
        for j in range(y, y + length):
            if matrix[i][j] == -1:
                if zero_configure or plus_configure:
                    return False
                min_configure = True
            elif matrix[i][j] == 0:
                if min_configure or plus_configure:
                    return False
                zero_configure = True
            else:
                if zero_configure or min_configure:
                    return False
                plus_configure = True

    return True


for i in range(N):
    matrix[i] = list(map(int, sys.stdin.readline().split()))

queue = deque()
queue.append([0, 0, N])

while queue:
    x, y, length = queue.popleft()
    if configure(x, y, length):
        if matrix[x][y] == -1:
            min_papers += 1
        elif matrix[x][y] == 0:
            zero_papers += 1
        else:
            plus_papers += 1

    else:
        length = length // 3
        for i in range(3):
            for j in range(3):
                queue.appendleft([x + i * length, y + j * length, length])

print(min_papers)
print(zero_papers)
print(plus_papers)