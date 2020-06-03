n = int(input())

n_arr = [[0 for _ in range(n)] for _ in range(n)]
d_arr = [[0 for _ in range(n)] for _ in range(n)]
arrow = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(n):
    temp = input()
    temp = temp.split()

    for j in range(len(temp)):
        n_arr[i][j] = int(temp[j])

def dfs(x, y):
    if d_arr[x][y] != 0:
        return d_arr[x][y]

    d_arr[x][y] = 1
    max_value = 0
    for i in range(4):
        x_edit = x + arrow[i][0]
        y_edit = y + arrow[i][1]

        if 0 <= x_edit < n and 0 <= y_edit < n:
            if n_arr[x][y] < n_arr[x_edit][y_edit]:
                temp_value = dfs(x_edit, y_edit)
                if max_value < temp_value:
                    max_value = temp_value
    d_arr[x][y] += max_value
    return d_arr[x][y]

for i in range(n):
    for j in range(n):
        if d_arr[i][j] == 0 :
            dfs(i, j)

max_arr = []
for i in range(n):
    max_arr.append(max(d_arr[i]))
print(max(max_arr))