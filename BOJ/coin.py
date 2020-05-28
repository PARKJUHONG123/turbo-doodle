temp = input()
temp = temp.split()
n, k = int(temp[0]), int(temp[1])
coin_arr = [0 for _ in range(n)]
d_arr = [0 for _ in range(k + 1)]

for i in range(n):
    coin_arr[i] = int(input())

d_arr[0] = 1

for i in range(n) :
    for j in range(k + 1):
        if j - coin_arr[i] >= 0:
            d_arr[j] = d_arr[j] + d_arr[j - coin_arr[i]]

print(d_arr[-1])