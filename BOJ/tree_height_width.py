import sys

class node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

n = int(sys.stdin.readline().strip())

tree_dict = dict()
root = None
for _ in range(n):
    value, left, right = map(int, sys.stdin.readline().split())
    tree_node = node(value, left, right)
    if not root:
        root = tree_node
    tree_dict[value] = tree_node

def pre_order(root, depth):
    print(root.value, depth)
    if root.left != -1:
        pre_order(tree_dict[root.left], depth + 1)
    if root.right != -1:
        pre_order(tree_dict[root.right], depth + 1)

pre_order(root, 1)