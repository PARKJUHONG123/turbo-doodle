T = int(input())

for _ in range(T):
    K = int(input())
    n_arr = [0 for _ in range(K)]

    temp = input()
    temp = temp.split()
    for i in range(K):
        n_arr[i] = int(temp[i])

    d_arr = [[0 for _ in range(K)] for _ in range(K)]
    s_arr = [[0 for _ in range(K)] for _ in range(K)]

    for i in range(K): # s_arr[i][j] : i에서 i까지의 합
        for j in range(i, K) :
            if i == j :
                s_arr[i][j] = n_arr[i]
            else :
                s_arr[i][j] = s_arr[i][j - 1] + n_arr[j]

    for hop in range(1, K):
        for i in range(K):
            if i + hop < K :
                min_value = d_arr[i][i] + d_arr[i + 1][i + hop] + s_arr[i][i + hop]
                for j in range(i, i + hop):
                    min_value = min(min_value, d_arr[i][j] + d_arr[j + 1][i + hop]  + s_arr[i][i + hop])

                d_arr[i][i + hop] = min_value

    print(d_arr[0][-1])

