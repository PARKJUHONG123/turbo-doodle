import sys

N, M = map(int, sys.stdin.readline().split())

m_arr = [0 for _ in range(N + 1)]
c_arr = [0 for _ in range(N + 1)]

temp = sys.stdin.readline().split()
for i in range(1, N + 1):
    m_arr[i] = int(temp[i - 1])

total_c = 0
temp = sys.stdin.readline().split()
for i in range(1, N + 1):
    c_arr[i] = int(temp[i - 1])
    total_c += c_arr[i]

d_arr = [[0 for _ in range(total_c + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(total_c + 1):
        if j >= c_arr[i]:
            d_arr[i][j] = max(d_arr[i - 1][j], d_arr[i-1][j - c_arr[i]] + m_arr[i])
        else :
            d_arr[i][j] = d_arr[i - 1][j]

min_j = total_c
for i in range(1, N + 1):
    for j in range(total_c + 1):
        if d_arr[i][j] >= M:
            min_j = min(min_j, j)

print(min_j)


