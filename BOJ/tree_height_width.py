import sys

class node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

n = int(sys.stdin.readline().strip())

tree_dict = dict()
for _ in range(n):
    value, left, right = map(int, sys.stdin.readline().split())
    tree_node = node(value, left, right)
    tree_dict[value] = tree_node

width = 1
max_dict, min_dict = dict(), dict()
depth_size = 0
def in_order(root, depth):
    global width, depth_size
    if root.left != -1:
        in_order(tree_dict[root.left], depth + 1)

    depth_size = max(depth_size, depth)
    max_dict[depth] = width
    if depth not in min_dict:
        min_dict[depth] = width
    width += 1

    if root.right != -1:
        in_order(tree_dict[root.right], depth + 1)

def find_root(param_node):
    param_value = param_node.value
    for key in tree_dict.keys():
        if tree_dict[key].left == param_value or tree_dict[key].right == param_value:
            return find_root(tree_dict[key])
    return param_node

root = find_root(tree_dict[value])
in_order(root, 1)
max_width, max_index = 0, 0
for depth in range(1, depth_size + 1):
    temp_width = max_dict[depth] - min_dict[depth] + 1
    if temp_width > max_width:
        max_width = temp_width
        max_index = depth
print(max_index, max_width)