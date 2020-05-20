#1 -> 1
#2 -> 3
#3 -> 5
#4 -> 7
#8 -> 171
#12 -> 2731

n = int(input())

d_arr = [0 for _ in range(n + 1)]

if (n == 1):
    d_arr[1] = 1
elif (n == 2):
    d_arr[1] = 1
    d_arr[2] = 3
else:
    d_arr[1] = 1
    d_arr[2] = 3
    minus = 1
    for j in range(3, n + 1):
        d_arr[j] = 2 * d_arr[j - 1] - minus
        minus += 2
print(d_arr)