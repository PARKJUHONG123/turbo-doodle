n = int(input())
n_arr = [0 for _ in range(n + 1)]
d_arr = [0 for _ in range(n + 1)] #i 까지 가장 크게 나온 값

temp = input()
if (n > 1):
    temp = temp.split()
    for i in range(1, n + 1):
        n_arr[i] = int(temp[i - 1])

    d_arr[0] = 0
    d_arr[1] = n_arr[1]

    for i in range(2, n + 1):
        max = 0
        for j in range(1, i + 1):
            if max < d_arr[i - j] + n_arr[j]:
                max = d_arr[i - j] + n_arr[j]
        d_arr[i] = max

    print(d_arr[-1])

else :
    print(temp)