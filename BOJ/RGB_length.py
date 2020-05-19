n = int(input())
n_arr = [[0 for _ in range(3)] for _ in range(n)]
d_arr = [[0 for _ in range(3)] for _ in range(n)]

for i in range(n):
    r, g, b = input().split()
    n_arr[i][0] = int(r)
    n_arr[i][1] = int(g)
    n_arr[i][2] = int(b)

for i in range(n):
    if (i == 0):
        d_arr[i][0] = n_arr[i][0]
        d_arr[i][1] = n_arr[i][1]
        d_arr[i][2] = n_arr[i][2]

    else:
        d_arr[i][0] = min(d_arr[i - 1][1], d_arr[i - 1][2]) + n_arr[i][0]
        d_arr[i][1] = min(d_arr[i - 1][0], d_arr[i - 1][2]) + n_arr[i][1]
        d_arr[i][2] = min(d_arr[i - 1][0], d_arr[i - 1][1]) + n_arr[i][2]

print(min(d_arr[n-1][0], d_arr[n-1][1], d_arr[n-1][2]))