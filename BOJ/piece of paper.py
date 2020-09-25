import sys
input = sys.stdin.readline

h, w = map(int, input().split())
mat = []
for i in range(h):
    mat.append(input())

ans = 0

for b in range(1 << h * w): # 2^(h*w)
    sum = 0
    for i in range(h):
        line_sum = 0
        for j in range(w):
            k = i * w + j
            if b & (1 << k): # 2^k == b
                sum += line_sum
                line_sum = 0
            else:
                line_sum = line_sum * 10 + int(mat[i][j])
        sum += line_sum

    for j in range(w):
        line_sum = 0
        for i in range(h):
            k = i * w + j
            if b & (1 << k):
                line_sum = line_sum * 10 + int(mat[i][j])
            else:
                sum += line_sum
                line_sum = 0
        sum += line_sum
    ans = max(ans, sum)
print(ans)