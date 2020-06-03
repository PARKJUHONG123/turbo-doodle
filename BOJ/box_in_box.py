n = int(input())
n_arr = [0 for _ in range(n)]
d_arr = [[] for _ in range(n)]

temp = input()
temp = temp.split()

for i in range(n):
    n_arr[i] = int(temp[i])

for i in range(n):
    for j in range(i):
        if len(d_arr[j]) > len(d_arr[i]) :
            if d_arr[j][-1] < n_arr[i] :
                d_arr[i] = d_arr[j][:]
    d_arr[i].append(n_arr[i])

max_len = 0
for i in range(n):
    if max_len < len(d_arr[i]) :
        max_len = len(d_arr[i])

print(max_len)