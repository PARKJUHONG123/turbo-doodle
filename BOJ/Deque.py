import sys
from collections import deque

N = int(sys.stdin.readline().strip())
queue = deque()
for _ in range(N):
    com = sys.stdin.readline().split()
    if len(com) == 2:
        if com[0] == 'push_front':
            queue.appendleft(com[1])
        elif com[0] == 'push_back':
            queue.append(com[1])
    else:
        if com[0] == 'pop_front':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif com[0] == 'pop_back':
            if queue:
                print(queue.pop())
            else:
                print(-1)
        elif com[0] == 'size':
            print(len(queue))
        elif com[0] == 'empty':
            print(0 if queue else 1)
        elif com[0] == 'front':
            print(queue[0] if queue else -1)
        elif com[0] == 'back':
            print(queue[-1] if queue else -1)
