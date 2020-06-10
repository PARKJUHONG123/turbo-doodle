t = int(input())

max_n = 67
d_arr = [0 for _ in range(max_n + 1)]

for i in range(max_n + 1):
    if i < 2 :
        d_arr[i] = 1
    elif i == 2 :
        d_arr[i] = 2
    elif i == 3 :
        d_arr[i] = 4
    else :
        d_arr[i] = d_arr[i - 1] + d_arr[i - 2] + d_arr[i - 3] + d_arr[i - 4]

for i in range(t):
    n = int(input())
    print(d_arr[n])