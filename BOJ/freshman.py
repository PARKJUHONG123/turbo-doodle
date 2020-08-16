import sys

N = int(sys.stdin.readline())
num = sys.stdin.readline().split()
d_arr = [[0 for _ in range(21)] for _ in range(N)]

for i in range(N):
    num[i] = int(num[i])

d_arr[0][num[0]] = 1
for i in range(1, N):
    for j in range(21):
        if d_arr[i - 1][j] != 0:
            if j - num[i] >= 0 :
                d_arr[i][j - num[i]] += (d_arr[i-1][j])
            if j + num[i] <= 20:
                d_arr[i][j + num[i]] += (d_arr[i-1][j])

print(d_arr[-1][0])