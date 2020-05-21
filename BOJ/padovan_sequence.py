count = int(input())

for i in range(count):
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(1)
    elif n == 3:
        print(1)
    else :
        d_arr = [0 for _ in range(n + 1)]
        d_arr[0] = 0
        d_arr[1] = 1
        d_arr[2] = 1
        d_arr[3] = 1

        for j in range(4, n + 1):
            d_arr[j] = d_arr[j - 2] + d_arr[j - 3]

        print(d_arr[-1])