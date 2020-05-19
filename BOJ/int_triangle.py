n = int(input())
n_arr = [[] for _ in range(n)]
d_arr = [[] for _ in range(n)]

for i in range(n):
    temp = input()
    temp = temp.split()
    n_arr[i] = temp
    for j in range(len(temp)):
        n_arr[i][j] = int(n_arr[i][j])
        d_arr[i].append(0)

d_arr[0][0] = n_arr[0][0]
for i in range(n):
    for j in range(i + 1):
        if (j == 0):
            d_arr[i][j] = d_arr[i - 1][j] + n_arr[i][j]
        elif (j == i):
            d_arr[i][j] = d_arr[i - 1][j - 1] + n_arr[i][j]
        else :
            d_arr[i][j] = max(d_arr[i - 1][j] + n_arr[i][j], d_arr[i - 1][j - 1] + n_arr[i][j])
print(max(d_arr[-1]))