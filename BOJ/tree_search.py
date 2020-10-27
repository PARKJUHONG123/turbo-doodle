import sys

class node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

N = int(sys.stdin.readline().strip())

tree_dict = dict()
root = None
for _ in range(N):
    value, left, right = sys.stdin.readline().split()
    NODE = node(value, left, right)
    if not root:
        root = NODE
    tree_dict[value] = NODE

order_list = [[] for _ in range(3)]

def pre_order(root):
    order_list[0].append(root.value)
    if root.left != '.':
        pre_order(tree_dict[root.left])
    if root.right != '.':
        pre_order(tree_dict[root.right])

def pre_order(root):
    order_list[0].append(root.value)
    if root.left != '.':
        pre_order(tree_dict[root.left])
    if root.right != '.':
        pre_order(tree_dict[root.right])

def in_order(root):
    if root.left != '.':
        in_order(tree_dict[root.left])
    order_list[1].append(root.value)
    if root.right != '.':
        in_order(tree_dict[root.right])

def post_order(root):
    if root.left != '.':
        post_order(tree_dict[root.left])
    if root.right != '.':
        post_order(tree_dict[root.right])
    order_list[2].append(root.value)

pre_order(root)
in_order(root)
post_order(root)

for value in order_list:
    print(''.join(value))
