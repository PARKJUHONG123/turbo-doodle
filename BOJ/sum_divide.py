temp = input()
temp = temp.split()

N = int(temp[0]) #20
K = int(temp[1]) #2
d_arr = [[0 for _ in range(N + 1)] for _ in range(K)]

for i in range(N + 1):
    d_arr[0][i] = 1

for i in range(1, K):
    for j in range(N + 1):
        d_arr[i][j] = (d_arr[i][j - 1] + d_arr[i - 1][j])

print(d_arr[-1][-1] % 1000000000)