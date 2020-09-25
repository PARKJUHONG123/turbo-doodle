import sys
from collections import deque
visited_len = 2000002
N, K = map(int, sys.stdin.readline().split())
visited = [-1 for _ in range(visited_len)]

def bfs():
    queue = deque()
    queue.append([-2, N, 0])

    while queue:
        before, t, t_count = queue.popleft()
        if t < visited_len:
            if visited[t] == -1:
                visited[t] = before
                if t == K:
                    print(t_count)
                    index = K
                    arr = []
                    while True:
                        value = visited[index]
                        if value == -2:
                            break
                        arr.append(value)
                        index = value
                    arr = list(reversed(arr))
                    arr.append(K)
                    print(*arr)

                    break
                queue.append([t, t * 2, t_count + 1])
                queue.append([t, t + 1, t_count + 1])
                if t >= 1:
                    queue.append([t, t - 1, t_count + 1])
bfs()
