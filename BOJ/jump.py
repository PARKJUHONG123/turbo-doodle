N = int(input())
n_arr = [[0 for _ in range(N)] for _ in range(N)]
d_arr = [[0 for _ in range(N)] for _ in range(N)]

d_arr[0][0] = 1
for i in range(N):
    temp = input()
    temp = temp.split()
    for j in range(N):
        n_arr[i][j] = int(temp[j])

for i in range(N):
    for j in range(N):
        temp = n_arr[i][j]
        if temp == 0:
            continue

        if i + temp < N:
            d_arr[i + temp][j] += d_arr[i][j]
        if j + temp < N:
            d_arr[i][j + temp] += d_arr[i][j]
print(d_arr[-1][-1])