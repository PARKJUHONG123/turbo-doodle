N = int(input())

n_arr = [0 for _ in range (N)]

if N == 1 :
    n_arr[0] = 3

elif N == 2 :
    n_arr[0] = 3
    n_arr[1] = 7

else :
    n_arr[0] = 3
    n_arr[1] = 7

    for i in range(2, N):
        n_arr[i] = 2 * n_arr[i - 1] + n_arr[i - 2]
        n_arr[i] %= 9901
print(n_arr[-1])