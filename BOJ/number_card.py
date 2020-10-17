import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()

M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
visited = [0 for _ in range(M)]

for i in range(M):
    start, end = 0, N

    while True:
        if start >= end:
            break
        mid = (start + end) // 2
        if cards[mid] == target[i]:
            visited[i] = 1
            break
        elif cards[mid] > target[i]:
            end = mid
        else:
            start = mid + 1

print(*visited)