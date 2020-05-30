temp = input()
temp = temp.split()

n = int(temp[0])
m = int(temp[1])
n_arr = [[0 for _ in range(m + 1)] for _ in range(n + 1) ]
d_arr = [[0 for _ in range(m + 1)] for _ in range(n + 1) ]

for i in range(1, n + 1):
    temp = input()
    temp = temp.split()
    for j in range(1, m + 1):
        n_arr[i][j] = int(temp[j - 1])

for i in range(n + 1):
    for j in range(m + 1):
        if j == 0 :
            d_arr[i][j] += n_arr[i][j]
        else :
            d_arr[i][j] += (n_arr[i][j] + d_arr[i][j-1])

k = int(input())
for i in range(k):
    temp = input()
    temp = temp.split()
    a_x = int(temp[0]) # 1
    a_y = int(temp[1]) # 2
    b_x = int(temp[2]) # 2
    b_y = int(temp[3]) # 3

    total = 0
    for j in range(a_x, b_x + 1):
        total += d_arr[j][b_y] - d_arr[j][a_y - 1]

    print(total)