temp = input()
N = len(temp)
d_arr = [0 for _ in range(N)]
error_value = False
fence = 1000000

if temp[0] == '0':
    error_value = True

else:
    if N == 0:
        error_value = True

    elif N == 1:
        d_arr[0] = 1

    elif N == 2:
        d_arr[0] = 1
        if temp[0] == '1':
            if temp[1] == '0':
                d_arr[1] = 1
            else:
                d_arr[1] = 2

        elif temp[0] == '2':
            if temp[1] == '0':
                d_arr[1] = 1
            elif '1' <= temp[1] <= '6':
                d_arr[1] = 2
            else:
                d_arr[1] = 1
        else:
            if temp[1] == '0':
                error_value = True
            else:
                d_arr[1] = 1

    else:
        d_arr[0] = 1
        if temp[0] == '1':
            if temp[1] == '0':
                d_arr[1] = 1
            else:
                d_arr[1] = 2

        elif temp[0] == '2':
            if temp[1] == '0':
                d_arr[1] = 1
            elif '1' <= temp[1] <= '6':
                d_arr[1] = 2
            else:
                d_arr[1] = 1
        else:
            if temp[1] == '0':
                error_value = True
            else:
                d_arr[1] = 1

        if error_value == False:
            for i in range(2, N):
                if temp[i - 1] == '0':
                    if temp[i] == '0':
                        error_value = True
                        break
                    else:
                        d_arr[i] = d_arr[i - 1]
                        d_arr[i] %= fence

                elif temp[i - 1] == '1':
                    if temp[i] == '0':
                        d_arr[i] = d_arr[i - 2]
                    else:
                        d_arr[i] = d_arr[i - 1] + d_arr[i - 2]
                    d_arr[i] %= fence

                elif temp[i - 1] == '2':
                    if temp[i] == '0':
                        d_arr[i] = d_arr[i - 2]
                    elif '1' <= temp[i] <= '6':
                        d_arr[i] = d_arr[i - 1] + d_arr[i - 2]
                    else:
                        d_arr[i] = d_arr[i - 1]
                    d_arr[i] %= fence

                else:
                    if temp[i] == '0':
                        error_value = True
                        break
                    else:
                        d_arr[i] = d_arr[i - 1]
                        d_arr[i] %= fence
if error_value == True:
    print(0)
else:
    print(d_arr[-1])