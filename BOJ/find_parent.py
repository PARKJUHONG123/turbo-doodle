import sys
from collections import deque
N = int(sys.stdin.readline().strip())

tree_dict = dict()
for i in range(1, N + 1):
    tree_dict[i] = []

for _ in range(N - 1):
    M, S = map(int, sys.stdin.readline().split())
    tree_dict[M].append(S)
    tree_dict[S].append(M)

parent = [-1 for _ in range(N + 1)]
def bfs(root):
    queue = deque()
    queue.append(root)
    parent[root] = 0
    while queue:
        node = queue.popleft()
        for value in tree_dict[node]:
            if parent[value] == -1:
                parent[value] = node
                queue.append(value)
bfs(1)
for i in range(2, N + 1):
    print(parent[i])
