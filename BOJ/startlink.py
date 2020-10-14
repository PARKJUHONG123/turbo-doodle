import sys
from collections import deque
F, S, G, U, D = map(int, sys.stdin.readline().split())

def bfs():
    visited = [False for _ in range(F + 1)]
    queue = deque()
    queue.append([S, 0])

    while queue:
        s, count = queue.popleft()
        if s == G:
            return count

        u, d = s + U, s - D
        if 0 < u <= F:
            if not visited[u]:
                visited[u] = True
                queue.append([u, count + 1])
        if 0 < d <= F:
            if not visited[d]:
                visited[d] = True
                queue.append([d, count + 1])
    return "use the stairs"

print(bfs())