import sys
from collections import deque
MAX_LENGTH = 100000
N, K = map(int, sys.stdin.readline().split())

def bfs():
    queue = deque()
    queue.append([N, 0])
    visited = [False for _ in range(MAX_LENGTH + 1)]

    while queue:
        n, count = queue.popleft()
        visited[n] = True
        left, right, duble = n - 1, n + 1, n * 2
        if n == K:
           return count

        if duble <= MAX_LENGTH:
            if not visited[duble]:
                queue.append([duble, count])

        if left >= 0:
            if not visited[left]:
                queue.append([left, count + 1])

        if right <= MAX_LENGTH:
            if not visited[right]:
                queue.append([right, count + 1])


print(bfs())
