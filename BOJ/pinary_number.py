n = int(input())

d_arr = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        d_arr[i] = 1
    elif i == 1:
        d_arr[i] = 1
    else:
        d_arr[i] = d_arr[i-1] + d_arr[i-2]

print(d_arr[-1])