import sys
N, M, V = map(int, sys.stdin.readline().split())

graph_list = [set([]) for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph_list[i].add(j)
    graph_list[j].add(i)

def dfs(graph_list, root):
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack += sorted(list(graph_list[node] - set(visited)), reverse=True)

    return visited

def bfs(graph_list, root):
    visited = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue += sorted(list(graph_list[node] - set(visited)))

    return visited

visited = dfs(graph_list, V)
for i in range(N):
    print(visited[i], end = '')
print()
visited = bfs(graph_list, V)
for i in range(N):
    print(visited[i], end = '')
