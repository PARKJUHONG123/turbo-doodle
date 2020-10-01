import sys
import copy

N, M, x, y, K = map(int, sys.stdin.readline().split())
matrix = [[] for _ in range(N)]
dice = [0 for _ in range(6)]

for i in range(N):
    matrix[i] = list(map(int, sys.stdin.readline().split()))

commands = list(map(int, sys.stdin.readline().split()))
floor_index = 5
right_index = 4
def print_dice():
    if matrix[x][y] == 0:
        matrix[x][y] = copy.deepcopy(dice[floor_index])
        if floor_index + 3 > 5:
            print(dice[floor_index - 3])
        else:
            print(dice[floor_index + 3])

    else:
        dice[floor_index] = copy.deepcopy(matrix[x][y])
        if floor_index + 3 > 5:
            print(dice[floor_index - 3])
        else:
            print(dice[floor_index + 3])
        matrix[x][y] = 0

for command in commands:
    if command == 1:
        if y + 1 < M:
            y = y + 1
            tmp = right_index
            if floor_index + 3 > 5:
                right_index = floor_index - 3
            else:
                right_index = floor_index + 3
            floor_index = tmp
            print_dice()
    elif command == 2:
        if y - 1 >= 0:
            y = y - 1
            tmp = floor_index
            if right_index + 3 > 5:
                floor_index = right_index - 3
            else:
                floor_index = right_index + 3
            right_index = tmp
            print_dice()
    elif command == 3:
        if x - 1 >= 0:
            x = x - 1
            if floor_index == 0:
                if right_index == 1:
                    floor_index = 2
                elif right_index == 2:
                    floor_index = 4
                elif right_index == 4:
                    floor_index = 5
                elif right_index == 5:
                    floor_index = 1

            elif floor_index == 1:
                if right_index == 0:
                    floor_index = 5
                elif right_index == 2:
                    floor_index = 0
                elif right_index == 3:
                    floor_index = 2
                elif right_index == 5:
                    floor_index = 3

            elif floor_index == 2:
                if right_index == 0:
                    floor_index = 1
                elif right_index == 1:
                    floor_index = 3
                elif right_index == 3:
                    floor_index = 4
                elif right_index == 4:
                    floor_index = 0

            elif floor_index == 3:
                if right_index == 1:
                    floor_index = 5
                elif right_index == 2:
                    floor_index = 1
                elif right_index == 4:
                    floor_index = 2
                elif right_index == 5:
                    floor_index = 4

            elif floor_index == 4:
                if right_index == 0:
                    floor_index = 2
                elif right_index == 2:
                    floor_index = 3
                elif right_index == 3:
                    floor_index = 5
                elif right_index == 5:
                    floor_index = 0

            elif floor_index == 5:
                if right_index == 0:
                    floor_index = 4
                elif right_index == 1:
                    floor_index = 0
                elif right_index == 3:
                    floor_index = 1
                elif right_index == 4:
                    floor_index = 3
            print_dice()
    elif command == 4:
        if x + 1 < N:
            x = x + 1
            if floor_index == 0:
                if right_index == 1:
                    floor_index = 5
                elif right_index == 2:
                    floor_index = 1
                elif right_index == 4:
                    floor_index = 2
                elif right_index == 5:
                    floor_index = 4

            elif floor_index == 1:
                if right_index == 0:
                    floor_index = 2
                elif right_index == 2:
                    floor_index = 3
                elif right_index == 3:
                    floor_index = 5
                elif right_index == 5:
                    floor_index = 0

            elif floor_index == 2:
                if right_index == 0:
                    floor_index = 4
                elif right_index == 1:
                    floor_index = 0
                elif right_index == 3:
                    floor_index = 1
                elif right_index == 4:
                    floor_index = 3

            elif floor_index == 3:
                if right_index == 1:
                    floor_index = 2
                elif right_index == 2:
                    floor_index = 4
                elif right_index == 4:
                    floor_index = 5
                elif right_index == 5:
                    floor_index = 1

            elif floor_index == 4:
                if right_index == 0:
                    floor_index = 5
                elif right_index == 2:
                    floor_index = 0
                elif right_index == 3:
                    floor_index = 2
                elif right_index == 5:
                    floor_index = 3

            elif floor_index == 5:
                if right_index == 0:
                    floor_index = 1
                elif right_index == 1:
                    floor_index = 3
                elif right_index == 3:
                    floor_index = 4
                elif right_index == 4:
                    floor_index = 0
            print_dice()


