import sys

N, L = map(int, sys.stdin.readline().split())
matrix = [[0 for _ in range(N)] for _ in range(N)]

clock_matrix = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    matrix[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        clock_matrix[j][i] = matrix[i][j]

count = 0
for i in range(N):
    install = [False for _ in range(N)]
    last_point, last_value = 0, matrix[i][0]
    for j in range(1, N):
        if matrix[i][j] != last_value:
            last_point, last_value = j, matrix[i][j]
    token = True
    for j in range(1, N):
        if matrix[i][j] == matrix[i][j - 1]:
            pass
        else:
            if abs(matrix[i][j] - matrix[i][j - 1]) == 1:
                if matrix[i][j] > matrix[i][j - 1]:
                    installed, differed = False, False
                    if j - L < 0:
                        token = False
                        break

                    for k in range(j - L, j):
                        if matrix[i][j - 1] != matrix[i][k]:
                            differed = True
                            break

                        if install[k]:
                            installed = True

                    if differed:
                        token = False
                        break

                    if installed:
                        token = False
                        break
                    else:
                        for k in range(j - L, j):
                            install[k] = True

                else:
                    installed, differed = False, False
                    if j + L > N:
                        token = False
                        break

                    for k in range(j, j + L):
                        if matrix[i][j] != matrix[i][k]:
                            differed = True
                            break

                        if install[k]:
                            installed = True

                    if differed:
                        token = False
                        break

                    if installed:
                        token = False
                        break
                    else:
                        for k in range(j, j + L):
                            install[k] = True

            else:
                token = False
                break
    if token:
        count += 1

for i in range(N):
    install = [False for _ in range(N)]
    last_point, last_value = 0, clock_matrix[i][0]
    for j in range(1, N):
        if clock_matrix[i][j] != last_value:
            last_point, last_value = j, clock_matrix[i][j]

    token = True
    for j in range(1, N):
        if clock_matrix[i][j] == clock_matrix[i][j - 1]:
            pass
        else:
            if abs(clock_matrix[i][j] - clock_matrix[i][j - 1]) == 1:
                if clock_matrix[i][j] > clock_matrix[i][j - 1]:
                    installed, differed = False, False
                    if j - L < 0:
                        token = False
                        break

                    for k in range(j - L, j):
                        if clock_matrix[i][j - 1] != clock_matrix[i][k]:
                            differed = True
                            break

                        if install[k]:
                            installed = True

                    if differed:
                        token = False
                        break

                    if installed:
                        token = False
                        break
                    else:
                        for k in range(j - L, j):
                            install[k] = True

                else:
                    installed, differed = False, False
                    if j + L > N:
                        token = False
                        break

                    for k in range(j, j + L):
                        if clock_matrix[i][j] != clock_matrix[i][k]:
                            differed = True
                            break

                        if install[k]:
                            installed = True

                    if differed:
                        token = False
                        break

                    if installed:
                        token = False
                        break
                    else:
                        for k in range(j, j + L):
                            install[k] = True

            else:
                token = False
                break
    if token:
        count += 1

print(count)