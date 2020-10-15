import sys
N, M = map(int, sys.stdin.readline().split())

A = [[0 for _ in range(M)] for _ in range(N)]
B = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    tmp = sys.stdin.readline()
    for j in range(M):
        A[i][j] = int(tmp[j])

for i in range(N):
    tmp = sys.stdin.readline()
    for j in range(M):
        B[i][j] = int(tmp[j])

count = 0
for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            count += 1

            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    A[x][y] = (0 if A[x][y] == 1 else 1)

for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            print(-1)
            exit()
print(count)