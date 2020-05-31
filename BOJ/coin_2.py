temp = input()
temp = temp.split()

n = int(temp[0])
k = int(temp[1])
n_arr = [0 for _ in range(n)]
d_arr = [0 for _ in range(k + 1)]

for i in range(n):
    n_arr[i] = int(input())
    if (n_arr[i] < len(d_arr)):
        d_arr[n_arr[i]] = 1

for i in range(1, k + 1):
    for j in range(n):
        if d_arr[i] != 0 :
            index = i + n_arr[j]
            if index < k + 1:
                if d_arr[index] == 0 :
                    d_arr[index] = d_arr[i] + 1
                else :
                    d_arr[index] = min(d_arr[i] + 1, d_arr[index])

if d_arr[-1] == 0:
    print(-1)
else :
    print(d_arr[-1])