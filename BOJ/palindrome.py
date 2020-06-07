import sys

N = int(input())

n_arr = [int(i) for i in sys.stdin.readline().split()]
d_arr = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    d_arr[i][i] = 1

for i in range(N - 1):
    if n_arr[i] == n_arr[i + 1]:
        d_arr[i][i + 1] = 1

for i in range(2, N): # i = 2
    for j in range(N - i): # j -> 0, 1, 2, 3, 4
        if d_arr[j + 1][j + i - 1] and n_arr[j + i] == n_arr[j]:
            d_arr[j][j + i] = 1

M = int(input())
for _ in range(M):
    x, y = [int(i) for i in sys.stdin.readline().split()]
    print(d_arr[x - 1][y - 1])
