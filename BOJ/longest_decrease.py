N = int(input())
n_arr = [0 for _ in range(N)]
d_arr = [[] for _ in range(N)]

temp = input()
temp = temp.split()

for i in range(N):
    n_arr[i] = int(temp[i])

for i in range(N):
    for j in range(i):
        if d_arr[j][-1] > n_arr[i]:
            if len(d_arr[j]) > len(d_arr[i]) :
                d_arr[i] = d_arr[j][:]
    d_arr[i].append(n_arr[i])

max_len = 0
for i in range(N):
    if max_len < len(d_arr[i]):
        max_len = len(d_arr[i])

print(max_len)