import sys
from collections import deque

MAX_LENGTH = 1000
S = int(sys.stdin.readline())
root = 1

def bfs():
    visited = [False for _ in range(MAX_LENGTH + 1)]
    queue = deque()
    queue.append([1, 0, 0])
    while queue:
        n, clip, count = queue.popleft()
        visited[n] = True
        if n == S:
            return count

        copy_clip, left = n + clip, n - 1

        if left >= 0:
            if not visited[left]:
                queue.append([left, clip, count + 1])

        if copy_clip <= MAX_LENGTH:
            if not visited[copy_clip]:
                queue.append([copy_clip, clip, count + 1])

        queue.append([n, n, count + 1])

print(bfs())
