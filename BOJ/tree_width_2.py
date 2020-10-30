import sys
N = int(sys.stdin.readline().strip())
tree_dict = dict()

if N == 1:
    print(0)
    exit()

for i in range(1, N + 1):
    tree_dict[i] = []

for _ in range(N - 1):
    start_vertex, next_vertex, weight = map(int, sys.stdin.readline().split())
    tree_dict[start_vertex].append([next_vertex, weight])
    tree_dict[next_vertex].append([start_vertex, weight])

def dfs(root):
    stack = list()
    visited = [False for _ in range(N + 1)]
    stack.append([root, 0])
    visited[root] = True
    max_index, max_weight = -1, -1

    while stack:
        start_vertex, weight = stack.pop()
        for value in tree_dict[start_vertex]:
            if not visited[value[0]]:
                visited[value[0]] = True
                stacked_weight = weight + value[1]
                stack.append([value[0], stacked_weight])
                if max_weight < stacked_weight:
                    max_index = value[0]
                    max_weight = stacked_weight
    return max_index, max_weight

first_index, first_weight = dfs(start_vertex)
final_index, final_weight = dfs(first_index)
print(final_weight)