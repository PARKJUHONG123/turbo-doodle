import sys

n, m = map(int, sys.stdin.readline().split())

matrix = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        matrix[i][j] = tmp[j]


def find_max(matrix, ex, ey):
    ret = 0
    for i in range(ex):
        for j in range(ey):
            if i + 3 < ex:
                tmp = 0
                for k in range(i, i + 4):
                    tmp += matrix[k][j]
                ret = max(ret, tmp)
            if j + 3 < ey:
                tmp = 0
                for k in range(j, j + 4):
                    tmp += matrix[i][k]
                ret = max(ret, tmp)

            if i + 2 < ex and j + 1 < ey:
                tmp = matrix[i][j] + matrix[i + 1][j] + matrix[i + 2][j]
                left = max(matrix[i][j + 1], max(matrix[i + 1][j + 1], matrix[i + 2][j + 1]))
                ret = max(ret, tmp + left)

                tmp = matrix[i][j] + matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 2][j + 1]
                ret = max(ret, tmp)

                tmp = matrix[i][j + 1] + matrix[i + 1][j + 1] + matrix[i + 1][j] + matrix[i + 2][j]
                ret = max(ret, tmp)

                tmp = matrix[i][j + 1] + matrix[i + 1][j + 1] + matrix[i + 2][j + 1]
                left = max(matrix[i][j], max(matrix[i + 1][j], matrix[i + 2][j]))
                ret = max(ret, tmp + left)

            if j + 2 < ey and i + 1 < ex:
                tmp = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2]
                left = max(matrix[i + 1][j], max(matrix[i + 1][j + 1], matrix[i + 1][j + 2]))
                ret = max(ret, tmp + left)

                tmp = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2]
                ret = max(ret, tmp)

                tmp = matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i][j + 1] + matrix[i][j + 2]
                ret = max(ret, tmp)

                tmp = matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2]
                left = max(matrix[i][j], max(matrix[i][j + 1], matrix[i][j + 2]))
                ret = max(ret, tmp + left)

            if i + 1 < ex and j + 1 < ey:
                tmp = matrix[i][j] + matrix[i + 1][j] + matrix[i][j + 1] + matrix[i + 1][j + 1]
                ret = max(ret, tmp)
    return ret


print(find_max(matrix, n, m))
