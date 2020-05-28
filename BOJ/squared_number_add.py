n = int(input())
d_arr = [i for i in range(n + 1)]
for i in range(1, n + 1) :
    j = 1
    index = i - j * j
    while 0 <= index :
        if d_arr[i] > d_arr[index] + 1 :
            d_arr[i] = d_arr[index] + 1
        j += 1
        index = i - j * j

print(d_arr[-1])