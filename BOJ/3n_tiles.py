N = int(input())
d_arr = [0 for _ in range(N + 1)]


if N == 1:
    d_arr[1] = 0

elif N == 2 :
    d_arr[2] = 3

elif N > 2 :
    d_arr[2] = 3

    for i in range(3, N + 1):
        if i % 2 == 0:
            d_arr[i] = 2

            for j in range(2, i) :
                if j % 2 == 0 :
                    if j == 2 :
                        d_arr[i] += 3 * d_arr[i - j]
                    else :
                        d_arr[i] += 2 * d_arr[i - j]

        else :
            d_arr[i] = 0

print(d_arr[-1])