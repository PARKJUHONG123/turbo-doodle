N = int(input())
d_arr = [0 for _ in range(N)]

if N == 1 :
    d_arr[0] = 1

elif N == 2 :
    d_arr[0] = 1
    d_arr[1] = 2

else :
    d_arr[0] = 1
    d_arr[1] = 2
    for i in range(2, N):
        d_arr[i] = d_arr[i - 1] + d_arr[i - 2]
        d_arr[i] = d_arr[i] % 15746

print(d_arr[-1])