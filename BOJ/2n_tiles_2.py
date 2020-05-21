temp = int(input())
n_arr = [0 for _ in range(temp + 1)]

if (temp == 1):
    n_arr[1] = 1

elif (temp == 2):
    n_arr[1] = 1
    n_arr[2] = 3

else:
    n_arr[1] = 1
    n_arr[2] = 3
    for j in range(3, temp + 1):
        n_arr[j] += n_arr[j-1] + 2 * n_arr[j-2]
print(n_arr[-1] % 10007)
