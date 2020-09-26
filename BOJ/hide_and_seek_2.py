import sys
from collections import deque
MAX_LENGTH = 100000
N, K = map(int, sys.stdin.readline().split())

min_count = -1
ways = 0
def bfs():
    global min_count, ways
    queue = deque()
    queue.append([N, 0])
    visited = [False for _ in range(MAX_LENGTH + 1)]

    while queue:
        n, count = queue.popleft()
        visited[n] = True
        left, right, duble = n - 1, n + 1, n * 2
        if n == K:
            if min_count == -1:
                min_count = count
                ways += 1
            else :
                if count > min_count:
                    continue
                else:
                    ways += 1

        if duble <= MAX_LENGTH:
            if not visited[duble]:
                queue.append([duble, count + 1])

        if left >= 0:
            if not visited[left]:
                queue.append([left, count + 1])

        if right <= MAX_LENGTH:
            if not visited[right]:
                queue.append([right, count + 1])


bfs()
print(min_count)
print(ways)
