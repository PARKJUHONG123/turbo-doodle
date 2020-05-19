n = int(input())

n_arr = [0 for _ in range(n)]
d_arr = [0 for _ in range(n)]

temp = input()
temp = temp.split()

for i in range(len(temp)):
    n_arr[i] = int(temp[i])

for i in range(n):
    d_arr[i] = max(d_arr[i - 1], 0) + n_arr[i]

print(max(d_arr))