import sys
A_VALUE = ord('A')

def check(nx, ny, element):
    if element in sudoku[nx]:
        return False

    for i in range(9):
        if element == sudoku[i][ny]:
            return False

    x, y = nx // 3 * 3, ny // 3 * 3

    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if i == nx or j == ny:
                continue
            if element == sudoku[i][j]:
                return False
    return True

def brute(x, y, left_tiles):
    global all_done
    if all_done:
        return
    if y >= 9:
        x, y = x + 1, 0
    if x >= 9:
        if left_tiles == 0:
            for value in sudoku:
                tmp = list(map(str, value))
                print(''.join(tmp))
            all_done = True
            return

    if sudoku[x][y] == 0:
        if x + 1 < 9:
            if sudoku[x + 1][y] == 0:
                for i in range(1, 10):
                    for j in range(i + 1, 10):
                        if not domino[i][j]:
                            if check(x, y, i) and check(x + 1, y, j):
                                domino[i][j] = True
                                sudoku[x][y], sudoku[x + 1][y] = i, j
                                brute(x, y + 1, left_tiles - 1)
                                domino[i][j] = False
                                sudoku[x][y], sudoku[x + 1][y] = 0, 0

                            if check(x, y, j) and check(x + 1, y, i):
                                domino[i][j] = True
                                sudoku[x][y], sudoku[x + 1][y] = j, i
                                brute(x, y + 1, left_tiles - 1)
                                domino[i][j] = False
                                sudoku[x][y], sudoku[x + 1][y] = 0, 0
        if y + 1 < 9:
            if sudoku[x][y + 1] == 0:
                for i in range(1, 10):
                    for j in range(i + 1, 10):
                        if not domino[i][j]:
                            if check(x, y, i) and check(x, y + 1, j):
                                domino[i][j] = True
                                sudoku[x][y], sudoku[x][y + 1] = i, j
                                brute(x, y + 1, left_tiles - 1)
                                domino[i][j] = False
                                sudoku[x][y], sudoku[x][y + 1] = 0, 0

                            if check(x, y, j) and check(x, y + 1, i):
                                domino[i][j] = True
                                sudoku[x][y], sudoku[x][y + 1] = j, i
                                brute(x, y + 1, left_tiles - 1)
                                domino[i][j] = False
                                sudoku[x][y], sudoku[x][y + 1] = 0, 0
    else:
        brute(x, y + 1, left_tiles)

index = 1
while True:
    N = int(sys.stdin.readline().strip())
    if N == 0:
        break
    left_tiles = 36 - N
    sudoku = [[0 for _ in range(9)] for _ in range(9)]
    domino = [[False for _ in range(10)] for _ in range(10)]
    for _ in range(N):
        U, LU, V, LV = sys.stdin.readline().split()
        U, V = int(U), int(V)
        if U < V:
            domino[U][V] = True
        else:
            domino[V][U] = True

        sudoku[ord(LU[0]) - A_VALUE][int(LU[1]) - 1] = U
        sudoku[ord(LV[0]) - A_VALUE][int(LV[1]) - 1] = V

    tmp = sys.stdin.readline().split()
    for i in range(1, 10):
        height, width = ord(tmp[i - 1][0]) - A_VALUE, int(tmp[i - 1][1]) - 1
        sudoku[height][width] = i

    print("Puzzle " + str(index))
    all_done = False
    brute(0, 0, left_tiles)
    index += 1
