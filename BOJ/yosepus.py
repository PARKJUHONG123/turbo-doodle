import sys
class circular_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor = None

    def add(self, node):
        if self.tail:
            node.next = self.head
            node.prev = self.tail
            self.tail.next = node
            self.head.prev = node
            self.tail = node

        else:
            self.head = node
            self.tail = self.head
            self.cursor = self.head

    def remove(self, K):
        for _ in range(K - 1):
            self.cursor = self.cursor.next
        prev, next = self.cursor.prev, self.cursor.next
        stack.append(self.cursor.value)
        self.cursor = next
        prev.next = next
        next.prev = prev

class node:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

N, K = map(int, sys.stdin.readline().split())
if N == K == 1:
    print("<1>")
else:
    stack = list()
    cll = circular_linked_list()
    for i in range(1, N + 1):
        cll.add(node(str(i)))

    for _ in range(N):
        cll.remove(K)

    answer = "<"
    for i in range(N):
        if i < N - 1:
            answer += (stack[i] + ', ')
        else:
            answer += (stack[i] + ">")
    print(answer)