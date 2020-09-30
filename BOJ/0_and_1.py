import sys
from collections import deque
T = int(sys.stdin.readline())
max_length = pow(10, 100)
def bfs():
    visited = [False for _ in range(N + 1)]
    queue = deque()
    queue.append(1)
    visited[1] = True

    while queue:
        M = queue.popleft()
        if M >= max_length:
            break
        a = M * 10
        an = a % N
        b = a + 1
        bn = b % N

        if not an:
            print(a)
            return

        if not bn:
            print(b)
            return

        if not visited[an]:
            queue.append(a)
            visited[an] = True

        if not visited[bn]:
            queue.append(b)
            visited[bn] = True
    print("BRAK")

for _ in range(T):
    tmp = sys.stdin.readline().strip()
    N = int(tmp)
    bfs()