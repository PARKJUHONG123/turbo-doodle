temp = input()
temp = temp.split()

x = int(temp[0])
y = int(temp[1])

n_arr = [[0 for _ in range(y + 1)] for _ in range(x + 1)]
d_arr = [[0 for _ in range(y + 1)] for _ in range(x + 1)]

for i in range(1, x + 1):
    temp = input()
    temp = temp.split()
    for j in range(1, len(temp) + 1):
        n_arr[i][j] = int(temp[j - 1])

for i in range(1, x + 1):
    for j in range(1, y + 1):
        d_arr[i][j] = max(d_arr[i][j - 1], d_arr[i -1][j], d_arr[i - 1][j - 1])
        d_arr[i][j] += n_arr[i][j]

print(d_arr[-1][-1])