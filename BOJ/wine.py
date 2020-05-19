n = int(input())
n_arr = [0 for _ in range(n)]
d_arr = [0 for _ in range(n)]

for i in range(n):
    n_arr[i] = int(input())

if n > 2 :
    d_arr[0] = n_arr[0]
    d_arr[1] = n_arr[0] + n_arr[1]
    d_arr[2] = max(n_arr[0] + n_arr[2], n_arr[1] + n_arr[2])
    d_arr[2] = max(d_arr[1], d_arr[2])

    for i in range(3, n):
        d_arr[i] = max(d_arr[i - 3] + n_arr[i] + n_arr[i - 1], n_arr[i] + d_arr[i - 2])
        d_arr[i] = max(d_arr[i-1] , d_arr[i])
    print(d_arr[-1])

else :
    if (n == 1) :
        print(n_arr[0])
    elif (n == 2) :
        print(n_arr[0] + n_arr[1])
