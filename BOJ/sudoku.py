import sys
N = 9

def check(nx, ny, element):
    if element in sudoku[nx]:
        return False

    for i in range(N):
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

sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
zeros = [(i, j) for i in range(N) for j in range(N) if sudoku[i][j] == 0]

def brute(index):
    if index == len(zeros):
        for value in sudoku:
            print(*value)
        sys.exit(0)

    for element in range(1, 10):
        nx = zeros[index][0]
        ny = zeros[index][1]

        if check(nx, ny, element):
            sudoku[nx][ny] = element
            brute(index + 1)
            sudoku[nx][ny] = 0
brute(0)