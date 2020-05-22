n = int(input())

t = [0 for _ in range(n)]
p = [0 for _ in range(n)]
d_t = [0 for _ in range(n)]
d_p = [0 for _ in range(n)]

for i in range(n):
    temp = input()
    temp = temp.split()
    t[i], p[i] = int(temp[0]), int(temp[1])
    d_t[i] = i - t[i]

print(d_t)

for i in range(n):
    if (d_t[i] >= 0):
        d_p[i] = p[i]
    else:
        d_p[i] = 0

print(d_p)

d_arr = [0 for _ in range(n + 1)]
for i in range(n):
    if (i + t[i] <= n):
        d_arr[ i + t[i] ] = max( d_arr[ i + t[i] ], d_arr[i] + p[i])
    print(i, d_arr)
