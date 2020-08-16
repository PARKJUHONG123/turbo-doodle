import sys

N, M, V = map(int, sys.stdin.readline().split())

graph_list = [set([]) for _ in range(N + 1)]

for i in range(M):
    S, E = map(int, sys.stdin.readline().split())
    graph_list[S].add(E)
    graph_list[E].add(S)

def dfs(graph_list, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if not n in visited:
            visited.append(n)
            stack += sorted(list(graph_list[n] - set(visited)), reverse = True)

    return visited

def bfs(graph_list, root):
    visited = []
    queue = [root]

    while queue:
        n = queue.pop(0)
        if not n in visited:
            visited.append(n)
            queue += sorted(list(graph_list[n] - set(visited)))

    return visited

visited = dfs(graph_list, V)

length = len(visited)
for i in range(len(visited)):
    print(visited[i], end = ' ')
print("")

visited = bfs(graph_list, V)
for i in range(len(visited)):
    print(visited[i], end = ' ')
