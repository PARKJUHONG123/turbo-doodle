import sys
import heapq

N = int(sys.stdin.readline().strip())
pair = [[[0, 0], 0] for _ in range(N)]
pair_dict = dict()
pair_set = set()

for i in range(N):
    left, height, right = map(int, sys.stdin.readline().split())
    pair[i][0][0], pair[i][0][1] = left, right
    pair[i][1] = height
    pair_set.add(left)
    pair_set.add(right)
pair.sort()
rx = list(pair_set)
rx.sort()

m = len(rx)
x = dict()
for i in range(len(rx)):
    x[rx[i]] = i

now, j = 0, 0
h = []

for i in range(m):
    while (j < N and x[pair[j][0][0]] <= i):
        heapq.heappush(h, (-pair[j][1], x[pair[j][0][1]]))
        j += 1
    next = 0
    while len(h):
        value = heapq.heappop(h)
        if i < value[1]:
            next = -value[0]
            heapq.heappush(h, value)
            break

    if now != next:
        now = next
        print(rx[i], now, end = ' ')