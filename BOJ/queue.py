import sys
from collections import deque
N = int(sys.stdin.readline().strip())
queue = deque()

for _ in range(N):
    com = sys.stdin.readline().split()

    if len(com) == 2:
        queue.append(com[1])
    else:
        if com[0] == "pop":
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif com[0] == "size":
            print(len(queue))
        elif com[0] == "empty":
            print(0 if queue else 1)
        elif com[0] == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif com[0] == "back":
            if queue:
                print(queue[-1])
            else:
                print(-1)