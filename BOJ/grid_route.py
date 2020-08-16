import sys
N, M, K = sys.stdin.readline().split()
N = int(N)
M = int(M)
K = int(K)

if K == 0 :
    K = 1

d_arr = [[0 for _ in range(M)] for _ in range(N)]
i_ic = (K - 1) // M
j_ic = (K - 1) % M

d_arr[0][0] = 1
for i in range(i_ic + 1):
    for j in range(j_ic + 1):
        if i - 1 >= 0 and j - 1 >= 0:
            d_arr[i][j] = d_arr[i - 1][j] + d_arr[i][j - 1]
        elif i - 1 >= 0:
            d_arr[i][j] = d_arr[i - 1][j]
        elif j - 1 >= 0:
            d_arr[i][j] = d_arr[i][j - 1]

for i in range(i_ic, N):
    for j in range(j_ic, M):
        if i - 1 >= i_ic and j - 1 >= j_ic:
            d_arr[i][j] = d_arr[i - 1][j] + d_arr[i][j - 1]
        elif i - 1 >= i_ic:
            d_arr[i][j] = d_arr[i - 1][j]
        elif j - 1 >= j_ic:
            d_arr[i][j] = d_arr[i][j - 1]

print(d_arr[-1][-1])