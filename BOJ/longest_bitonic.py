N = int(input())
n_arr = [0 for _ in range(N)]
r_arr = [0 for _ in range(N)]

d_arr = [[] for _ in range(N)]
i_arr = [[] for _ in range(N)]

temp = input()
temp = temp.split()

for i in range(N):
    n_arr[i] = int(temp[i])
    r_arr[N - 1 - i] = n_arr[i]

for i in range(N):
    for j in range(i):
        if d_arr[j][-1] < n_arr[i]:
            if len(d_arr[j]) > len(d_arr[i]) :
                d_arr[i] = d_arr[j][:]
        if i_arr[j][-1] < r_arr[i]:
            if len(i_arr[j]) > len(i_arr[i]):
                i_arr[i] =  i_arr[j][:]

    d_arr[i].append(n_arr[i])
    i_arr[i].append(r_arr[i])

max_len = 0
for i in range(N):
    i_arr[N - 1 - i].reverse()
    temp = (d_arr[i][: -1] + i_arr[N - 1 - i])
    if max_len < len(temp):
        max_len = len(temp)

print(max_len)