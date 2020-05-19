n = int(input())
d_arr = [0 for _ in range(10)]
n_arr = [0 for _ in range(10)]

for i in range(0, 10):
    d_arr[i] = 1
    n_arr[i] = 1

for i in range(n - 1):
    for j in range(0, 10):
        if j == 0:
            d_arr[j] = n_arr[1]
        elif j == 9:
            d_arr[j] = n_arr[8]
        else:
            d_arr[j] = n_arr[j - 1] + n_arr[j + 1]
    for j in range(0, 10):
        n_arr[j] = d_arr[j]

total = 0
for i in range(1, 10):
    total += n_arr[i]

print(total % 1000000000)