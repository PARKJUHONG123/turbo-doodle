import sys

N, M = list(map(int, sys.stdin.readline().split()))
graph = dict()
for i in range(N):
    graph[i + 1] = []

for _ in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, root):
    visited = set()
    stack = []
    stack.append(root)

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.add(n)
            for value in reversed(graph[n]):
                stack.append(value)
    return visited

ret = [-1 for _ in range(N + 1)]
count = 1
for i in range(1, N + 1):
    if ret[i] == -1:
        dfs_ret = dfs(graph, i)
        for value in dfs_ret:
            ret[value] = count
        count += 1
print(max(ret))
