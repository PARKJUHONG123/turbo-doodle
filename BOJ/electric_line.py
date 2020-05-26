n = int(input())

line = []
for i in range(n):
    temp = input()
    temp = temp.split()
    line.append([int(temp[0]), int(temp[1])])

line_temp = [0, 0]
for i in range(n):
    for j in range(i):
        if line[i][0] < line[j][0]:
            line_temp[0] = line[i][0]
            line_temp[1] = line[i][1]
            line[i][0] = line[j][0]
            line[i][1] = line[j][1]
            line[j][0]= line_temp[0]
            line[j][1]= line_temp[1]

d_arr = [[] for _ in range(n)]
for i in range(n):
    if i == 0:
        d_arr[i].append(line[i][1])
    else :
        if len(d_arr[i]) == 0:
            d_arr[i].append(line[i][1])
        for j in range(i):
            if d_arr[j][-1] < line[i][1]:
                if len(d_arr[i]) - 1 < len(d_arr[j]):
                    d_arr[i] = d_arr[j] + [line[i][1]]

max_length = 0
for i in range(n):
    if max_length < len(d_arr[i]):
        max_length = len(d_arr[i])

print(n - max_length)
print(d_arr)
