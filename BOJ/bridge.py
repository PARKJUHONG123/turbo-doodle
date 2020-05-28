count = int(input())

for _ in range(count):
    temp = input()
    temp = temp.split()

    N = int(temp[0])
    M = int(temp[1])

    d_arr = [0 for _ in range(N)]

    # M c N

    for i in range(N):
        if i == 0 :
            d_arr[i] = M
        else :
            d_arr[i] = d_arr[i-1] * (M - i) / (i + 1)

    print(int(d_arr[-1]))
