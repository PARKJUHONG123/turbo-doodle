n = int(input())

temp = input()
temp = temp.split()

for i in range(n):
    temp[i] = int(temp[i])

d_arr = [[] for i in range(n)]
total_arr = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if d_arr[j][-1] < temp[i]:
            if sum(d_arr[i]) < sum(d_arr[j]) :
                d_arr[i] = d_arr[j][:]
    d_arr[i].append(temp[i])
    total_arr[i] = sum(d_arr[i])
print(max(total_arr))