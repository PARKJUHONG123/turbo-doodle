import sys
N, M = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, start):
    visited = [False for _ in range(N)]
    stack = []
    stack.append([start, 0])

    while stack:
        n, count = stack.pop()
        if visited[n] == False:
            if count >= 4:
                print("1")
                exit()
            visited[n] = True
            for value in reversed(graph[n]):
                stack.append([value, count + 1])

for i in range(N):
    dfs(graph, i)
print("0")

'''
visited = [False for _ in range(N)]
def dfs(root, depth):
    visited[root] = True
    if depth >= 4:
        print("1")
        exit()
    for value in graph[root]:
        if not visited[value]:
            visited[value] = True
            dfs(value, depth + 1)
            visited[value] = False

for i in range(N):
    dfs(i, 0)
    visited[i] = False
print("0")
'''