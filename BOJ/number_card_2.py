import sys
from collections import Counter
N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
visited = [0 for _ in range(M)]

C = Counter(cards)

for i in range(M):
    if target[i] in C:
        visited[i] = C[target[i]]

print(*visited)