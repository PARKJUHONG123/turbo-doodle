import heapq
import sys
a_heap, b_heap = [], []

N = int(sys.stdin.readline().strip())
for _ in range(N):
    a, h, b = map(int, sys.stdin.readline().split())
    if a_heap:
        while a_heap:
            value = heapq.heappop(a_heap)
            heapq.heappush(b_heap, value)
        heapq.heappush(b_heap, (a, h))
        heapq.heappush(b_heap, (b, 0))

    else:
        if b_heap:
            while b_heap:
                value = heapq.heappop(b_heap)
                print(value[0])
                heapq.heappush(a_heap, value)
        else:
            heapq.heappush(a_heap, (a, h))
            heapq.heappush(a_heap, (b, 0))

print(a_heap)
print(b_heap)