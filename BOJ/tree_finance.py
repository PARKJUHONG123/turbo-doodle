import sys
N, M, K = map(int, sys.stdin.readline().split())
N = N + 2
feed = [[0 for _ in range(N)] for _ in range(N)]
left_feed = [[5 for _ in range(N)] for _ in range(N)]
land = [[[] for _ in range(N)] for _ in range(N)]
add_baby = [[0 for _ in range(N)] for _ in range(N)]

start_n, end_n = 1, N - 1

for i in range(start_n, end_n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(start_n, end_n):
        feed[i][j] = temp[j - 1]

for i in range(M):
    temp = list(map(int, sys.stdin.readline().split()))
    land[temp[0]][temp[1]].append(temp[2])

def round_baby(x, y):
    for a in range(-1, 2):
        for b in range(-1, 2):
            if not (a == 0 and b == 0):
                add_baby[x + a][y + b] += 1

for _ in range(K):
    for i in range(start_n, end_n):
        for j in range(start_n, end_n):
            if land[i][j]:
                land[i][j].sort()
                alive_index = -1
                token = False
                for k in range(len(land[i][j])):
                    if left_feed[i][j] >= land[i][j][k] and not token:
                        left_feed[i][j] -= land[i][j][k]
                        land[i][j][k] += 1
                        if land[i][j][k] % 5 == 0:
                            round_baby(i, j)
                        alive_index = k
                    else:
                        token = True
                        left_feed[i][j] += land[i][j][k] // 2

                if alive_index == -1:
                    land[i][j] = []
                else:
                    land[i][j] = land[i][j][: (alive_index + 1)]

    for i in range(start_n, end_n):
        for j in range(start_n, end_n):
            left_feed[i][j] += feed[i][j]
            if add_baby[i][j] > 0:
                for _ in range(add_baby[i][j]):
                    land[i][j].append(1)
                add_baby[i][j] = 0


total = 0
for i in range(start_n, end_n):
    for j in range(start_n, end_n):
        total += len(land[i][j])
print(total)