import sys
from collections import deque

x_dir = [-1, 0, 0, 1]
y_dir = [0, -1, 1, 0]

N = int(sys.stdin.readline().strip())
matrix = [[] for _ in range(N)]

def bfs():
    queue = deque()
    queue.append([0, 0])
    visited = [[False for _ in range(N)] for _ in range(N)]

    while queue:
        dx, dy = queue.popleft()
        if dx == N - 1 and dy == N - 1:
            return True
        for i in range(4):
            rx, ry = dx + x_dir[i], dy + y_dir[i]
            if 0 <= rx < N and 0 <= ry < N:
                if left <= matrix[rx][ry] <= right and not visited[rx][ry]:
                    visited[rx][ry] = True
                    queue.append([rx, ry])

    return False


left_min, right_max = 987654321, -987654321
for i in range(N):
    matrix[i] = list(map(int, sys.stdin.readline().split()))
    right_max = max(max(matrix[i]), right_max)
    left_min = min(min(matrix[i]), left_min)
left_max, right_min = min(matrix[0][0], matrix[-1][-1]), max(matrix[0][0], matrix[-1][-1])
left, right = left_min, right_min

answer = sys.maxsize
while left_min <= left <= left_max and right_min <= right <= right_max:
    if bfs():
        answer = min(answer, right - left)
        left += 1
    else:
        right += 1
print(answer)