n = int(input())
n_arr = input()
n_arr = n_arr.split()

for i in range(n):
    n_arr[i] = int(n_arr[i])

d_arr = [1 for _ in range(n)]

max = 1
for i in range(1, n):
    min = 0
    for j in range(i):
        if (n_arr[i] > n_arr[j]):
            if (min < d_arr[j]):
                min = d_arr[j]
    d_arr[i] = min + 1
    if (max < d_arr[i]):
        max = d_arr[i]

print(max)