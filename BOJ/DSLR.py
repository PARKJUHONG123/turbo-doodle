import sys
from _collections import deque
T = int(sys.stdin.readline())

def trace_back(visited, turned, start, final):
    ret, arr = "", []
    while start != final:
        arr.append(start)
        start = visited[start]
    arr.append(final)
    arr.reverse()

    for i in range(1, len(arr)):
        ret += turned[arr[i]]
    return ret

def bfs(A, B):
    visited = [-1 for _ in range(10000)]
    turned = ["N" for _ in range(10000)]

    queue = deque()
    queue.append(A)
    visited[A] = -2

    while queue:
        n = queue.popleft()
        if n == B:
            return trace_back(visited, turned, B, A)

        #D
        value = (n * 2) % 10000
        if visited[value] == -1:
            queue.append(value)
            visited[value] = n
            turned[value] = "D"
        #S
        value = n - 1
        if value == -1:
            value = 9999
        if visited[value] == -1:
            queue.append(value)
            visited[value] = n
            turned[value] = "S"

        #L
        value = (n % 1000) * 10 + n // 1000
        if visited[value] == -1:
            queue.append(value)
            visited[value] = n
            turned[value] = "L"

        #R
        value = (n % 10) * 1000 + n // 10
        if visited[value] == -1:
            queue.append(value)
            visited[value] = n
            turned[value] = "R"

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(bfs(A, B))
