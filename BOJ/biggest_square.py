temp = input()
temp = temp.split()

n = int(temp[0])
m = int(temp[1])

n_arr = [[0 for _ in range(m)] for _ in range(n)]
d_arr = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    temp = input()
    for j in range(m):
        n_arr[i][j] = int(temp[j])

d_arr = n_arr[:]

if m == 0 :
    print(0)
else :
    for i in range(n):
        for j in range(m):
            if i - 1 >= 0 and j - 1 >= 0 :
                if d_arr[i][j] > 0 and d_arr[i - 1][j] > 0 and d_arr[i][j - 1] > 0 and d_arr[i - 1][j - 1] > 0 :
                    d_arr[i][j] = min(d_arr[i - 1][j], d_arr[i][j - 1], d_arr[i - 1][j - 1]) + 1

    max_value = [0 for _ in range(n)]
    for i in range(n):
        max_value[i] = max(d_arr[i])
    print(max(max_value) ** 2)