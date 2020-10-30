import sys

def dfs(root):
    visited = [False for _ in range(V + 1)]
    stack = list()
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
                    max_weight = stacked_weight
                    max_index = value[0]
    return max_index, max_weight

V = int(sys.stdin.readline().strip())
tree_dict = dict()

for _ in range(V):
    input_list = list(map(int, sys.stdin.readline().split()))
    start_vertex = input_list[0] - 1
    tree_dict[start_vertex] = []
    index = 1

    while input_list[index] != -1:
        approach_vertex = input_list[index] - 1
        distance = input_list[index + 1]
        tree_dict[start_vertex].append([approach_vertex, distance])
        index += 2

first_index, first_weight = dfs(start_vertex)
final_index, final_weight = dfs(first_index)
print(final_weight)