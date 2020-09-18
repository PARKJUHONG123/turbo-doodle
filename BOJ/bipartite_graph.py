import sys
from collections import deque
K = int(sys.stdin.readline())

def dfs(graph, root):
    stack.append(root)
    visited[root] = 1

    while stack:
        n = stack.pop()
        for value in graph[n]:
            if visited[value] == 0:
                visited[value] = -1 * visited[n]
                stack.append(value)
            elif visited[value] == visited[n]:
                return False
    return True

def bfs(graph, root):
    queue.append(root)
    visited[root] = 1

    while queue:
        n = queue.popleft()
        for value in graph[n]:
            if visited[value] == 0:
                visited[value] = -1 * visited[n]
                queue.append(value)
            elif visited[value] == visited[n]:
                return False
    return True

for _ in range(K):
    V, E = list(map(int, sys.stdin.readline().split()))
    graph = dict()

    stack = []
    visited_stack = [0 for _ in range(V + 1)]

    queue = deque()
    visited = [0 for _ in range(V + 1)]

    for i in range(V):
        graph[i + 1] = list()

    for _ in range(E):
        a, b = list(map(int, sys.stdin.readline().split()))
        graph[a].append(b)
        graph[b].append(a)

    token = True
    for i in range(1, V + 1):
        if visited[i] == 0:
#            token = bfs(graph, i)
            token = dfs(graph, i)
            if token == False:
                break
    if token == False:
        print("NO")
    else:
        print("YES")
