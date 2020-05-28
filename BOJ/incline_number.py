N = int(input())

d_arr = [10 - i for i in range(10)]
total = 0
for i in range(10):
    total += d_arr[i]
for _ in range(N - 1):
    for i in range(10):
        temp_value = d_arr[i]
        d_arr[i] = total
        total -= temp_value

    for i in range(10):
        total += d_arr[i]

print(d_arr[0] % 10007)