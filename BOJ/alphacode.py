temp = input()

if temp[0] == '0':
    print(0)

elif "00" in temp :
    print(0)

else :
    temp = temp.replace("10", "A")
    temp = temp.replace("20", "B")
    N = len(temp)

    c_arr = [0 for _ in range(N)]
    d_arr = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N - 1):
        if temp[i] == 'A' or temp[i] == 'B' or temp[i + 1] == 'A' or temp[i + 1] == 'B':
            continue

        if 0 < int(temp[i]) <= 2 and int(temp[i + 1]) <= 6:
            c_arr[i] += 1

    for i in range(N):
        d_arr[i][i] = 1

    for hop in range(1, N):
        for i in range(N - hop):
            for k in range(hop):
                d_arr[i][i + hop] = max(d_arr[i][i + hop], d_arr[i][i + k] * d_arr[i + (1 + k)][i + hop] + c_arr[i + k])
            d_arr[i][i + hop] %= 1000000
    print(d_arr[0][-1])