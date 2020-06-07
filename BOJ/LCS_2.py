str1 = input()
str2 = input()

d_arr = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
s_arr = [["" for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            d_arr[i][j] = d_arr[i - 1][j - 1] + 1
            s_arr[i][j] = s_arr[i - 1][j - 1] + str1[i - 1]

        else :
            if d_arr[i - 1][j] > d_arr[i][j - 1]:
                d_arr[i][j] = d_arr[i - 1][j]
                s_arr[i][j] = s_arr[i - 1][j]
            else :
                d_arr[i][j] = d_arr[i][j - 1]
                s_arr[i][j] = s_arr[i][j - 1]


print(d_arr[-1][-1])
if d_arr[-1][-1] != 0:
    print(s_arr[-1][-1])

