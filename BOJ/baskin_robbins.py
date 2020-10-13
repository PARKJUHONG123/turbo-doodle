import sys

N, M = map(int, sys.stdin.readline().split())

if N < 3:
    print(0)
    exit()

total_length = (N * (N - 1) * (N - 2)) // 6
not_interested_set = set()
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(1, N + 1):
        if i != a and i != b:
            not_interested_set.add(tuple(sorted([a, b, i])))
print(total_length - len(not_interested_set))
