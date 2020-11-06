import sys
from collections import deque
K = int(sys.stdin.readline().strip())

count = 0
queue = deque()
def hanoi(number, from_, by_, to_):
    global count
    if number == 1:
        queue.append([from_, to_])
    else:
        hanoi(number - 1, from_, to_, by_)
        queue.append([from_, to_])
        hanoi(number - 1, by_, from_, to_)

hanoi(K, "1", "2", "3")
print(len(queue))
while queue:
    print(*(queue.popleft()))