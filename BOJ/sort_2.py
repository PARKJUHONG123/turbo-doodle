import sys
import heapq

N = int(sys.stdin.readline().strip())
h = list()
for _ in range(N):
    temp = int(sys.stdin.readline().strip())
    heapq.heappush(h, temp)

for _ in range(N):
    print(heapq.heappop(h))