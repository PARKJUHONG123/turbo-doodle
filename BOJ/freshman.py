import sys

N = int(sys.stdin.readline())
num = sys.stdin.readline().split()
d_arr = [[0 for _ in range(21)] for _ in range(N)]

for i in range(N):
    num[i] = int(num[i])
<<<<<<< HEAD

d_arr[0][num[0]] = 1
=======
d_arr[0][num[0]] = 1

>>>>>>> a36318892441c77bcfccb966c313e79c23e75ca0
for i in range(1, N):
    for j in range(21):
        if d_arr[i - 1][j] != 0:
            if j - num[i] >= 0 :
                d_arr[i][j - num[i]] += (d_arr[i-1][j])
            if j + num[i] <= 20:
                d_arr[i][j + num[i]] += (d_arr[i-1][j])

<<<<<<< HEAD
print(d_arr[-1][0])
=======
print(d_arr[-2][num[-1]])
>>>>>>> a36318892441c77bcfccb966c313e79c23e75ca0
