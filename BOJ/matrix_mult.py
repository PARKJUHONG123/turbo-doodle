import sys

N = int(sys.stdin.readline())
n_arr = [[0, 0] for _ in range(N)]
d_arr = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    n_arr[i][0], n_arr[i][1] = sys.stdin.readline().split()
    n_arr[i][0] = int(n_arr[i][0])
    n_arr[i][1] = int(n_arr[i][1])

for hop in range(1, N):
    for i in range(N - hop):
        min_value = d_arr[i][i] + d_arr[i + 1][i + hop] + n_arr[i][0] * n_arr[i][1] * n_arr[i + hop][1]
        for k in range(i + 1, i + hop):
            min_value = min(min_value, d_arr[i][k] + d_arr[k + 1][i + hop] + n_arr[i][0] * n_arr[k][1] * n_arr[i + hop][1])
        d_arr[i][i + hop] += min_value

print(d_arr[0][-1])