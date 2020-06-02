def dfs_decline(n_, d_, x, y, ar_):
    if x == 0 and y == 0:
        return 1

    if d_[x][y] != -1:
        return d_[x][y]

    d_[x][y] = 0
    for i in range(4):
        x_value = x + ar_[i][0]
        y_value = y + ar_[i][1]

        if 0 <= x_value < M and 0 <= y_value < N:
                if n_[x][y] < n_[x_value][y_value]:
                    d_[x][y] += dfs_decline(n_, d_, x_value, y_value, ar_)
    return d_[x][y]

temp = input()
temp = temp.split()
M = int(temp[0])
N = int(temp[1])

n_arr = [[0 for _ in range(N)] for _ in range(M)]
arrow = [[-1, 0], [+1, 0], [0, -1], [0, +1]]
d_arr = [[-1 for _ in range(N)] for _ in range(M)]

for i in range(M):
    temp = input()
    temp = temp.split()
    for j in range(N):
        n_arr[i][j] = int(temp[j])
print(dfs_decline(n_arr, d_arr, M - 1, N - 1, arrow))