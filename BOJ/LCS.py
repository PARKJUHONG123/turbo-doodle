str1 = input()
str2 = input()
d_arr = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            d_arr[i][j] = d_arr[i - 1][j - 1] + 1
        else :
            d_arr[i][j] = max(d_arr[i - 1][j], d_arr[i][j - 1])

for i in range(len(str1) + 1):
    print(d_arr[i])