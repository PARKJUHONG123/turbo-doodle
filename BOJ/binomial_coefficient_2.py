temp = input()
temp = temp.split()

N = int(temp[0])
K = int(temp[1])

d_arr = [0 for _ in range(K + 1)]

d_arr[0] = 1

for i in range(K):
    d_arr[i + 1] = (N - i) * d_arr[i] // (i + 1)

print(d_arr[-1] % 10007)