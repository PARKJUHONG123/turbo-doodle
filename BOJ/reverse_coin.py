import sys

N = int(sys.stdin.readline())
matrix = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    tmp = sys.stdin.readline()
    for j in range(N):
        matrix[i][j] = (False if tmp[j] == 'H' else True)

answer = 98765321
for k in range(1 << N):
    total = 0
    for j in range(N):
        now_t = 0
        for i in range(N):
            now = matrix[i][j]

            if (1 << i) & k:
                print(i, j)
                now = (False if matrix[i][j] else True)
            if now:
                now_t += 1
        print("")
        total += min(now_t, N - now_t)
    answer = min(answer, total)
print(answer)