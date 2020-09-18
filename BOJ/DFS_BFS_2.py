import sys
from collections import deque

N, M, V = list(map(int, sys.stdin.readline().split()))

graph = dict()
for i in range(N):
    graph[i + 1] = []

for _ in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, root):
    visited = []
    stack = []
    stack.append(root)

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            for value in reversed(sorted(graph[n])):
                if value not in visited:
                    stack.append(value)
    return visited


def bfs(graph, root):
    visited = []
    queue = deque([])
    queue.append(root)

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            for value in sorted(graph[n]):
                if value not in visited:
                    queue.append(value)
    return visited

dfs_list = list(map(str, dfs(graph, V)))
print(" ".join(dfs_list))
bfs_list = list(map(str, bfs(graph, V)))
print(" ".join(bfs_list))
