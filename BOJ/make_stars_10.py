import sys
N = int(sys.stdin.readline().strip())

def change_to_target(N):
    for i in range(1, 8):
        if pow(3, i) == N:
            return i
target = change_to_target(N)
matrix = [['*' for _ in range(N)] for _ in range(N)]
dp = [list() for _ in range(8)]
dp[0] = ['*']

def set_dp(length):
    if length == target + 1:
        return
    distance = pow(3, length)
    dp[length] = [['' for _ in range(distance)] for _ in range(distance)]

    third_distance = distance // 3
    x, y = third_distance, third_distance
    for i in range(0, distance, third_distance):
        for j in range(0, distance, third_distance):
            if i == j == third_distance:
                continue
            for k in range(third_distance):
                for l in range(third_distance):
                    dp[length][i + k][j + l] = dp[length - 1][k][l]

    for i in range(x, x * 2):
        for j in range(y, y * 2):
            dp[length][i][j] = ' '
    set_dp(length + 1)
set_dp(1)

for value in dp[target]:
    print(''.join(value))
