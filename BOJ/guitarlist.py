import sys

N, S, M = map(int, sys.stdin.readline().split())
V = list(map(int, sys.stdin.readline().split()))

last_volume = set()
last_volume.add(S)

for i in range(N):
    now_volume = set()
    for value in last_volume:
        if 0 <= value - V[i] <= M:
            now_volume.add(value - V[i])
        if 0 <= value + V[i] <= M:
            now_volume.add(value + V[i])
    last_volume = now_volume
    if not last_volume:
        print(-1)
        exit()
print(max(last_volume))