import sys
INF = 987654321
N, M = map(int, sys.stdin.readline().split())
friend_set = [set() for _ in range(N)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    a, b = A - 1, B - 1
    friend_set[a].add(b)
    friend_set[b].add(a)

min_value = INF
for i in range(N):
    i_length = len(friend_set[i])
    if i_length < 2:
        continue
    for j in range(i + 1, N):
        j_length = len(friend_set[j])
        if j_length < 2 or i not in friend_set[j]:
            continue
        for k in range(j + 1, N):
            k_length = len(friend_set[k])
            if k_length < 2 or i not in friend_set[k] or j not in friend_set[k]:
                continue
            min_value = min(min_value, i_length + j_length + k_length - 6)
print(min_value if min_value != INF else -1)