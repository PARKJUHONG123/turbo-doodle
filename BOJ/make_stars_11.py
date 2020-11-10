import sys
N = int(sys.stdin.readline().strip())
def change_to_length(N):
    for i in range(11):
        if 3 * (2 ** i) == N:
            return i

target = change_to_length(N)
total_length = N * 2 - 1
dp = [list() for _ in range(11)]
dp[0] = [['*'], ['*', ' ', '*'], ['*', '*', '*', '*', '*']]

def set_dp(length):
    if length == target + 1:
        return
    dp[length] = [[' ' for _ in range(2 * i + 1)] for i in range(3 * (2 ** length))]
    count = 1
    end_point = 3 * (2 ** length)
    distance = end_point // 2

    for i in range(0, end_point, distance):
        for inner_i in range(i, i + distance):
            double_inner_i = 2 * inner_i
            double_i = 2 * i

            for j in range(double_inner_i - double_i + 1):
                dp[length][inner_i][j] = dp[length - 1][inner_i - i][j]
            if count == 2:
                for j in range(double_i, double_inner_i + 1):
                    dp[length][inner_i][j] = dp[length - 1][inner_i - i][j - double_i]
        count += 1

    set_dp(length + 1)
set_dp(1)

matrix = [[' ' for _ in range(total_length)] for _ in range(N)]
index = 0
for value in reversed(dp[target]):
    length = len(value)
    for i in range(length):
        matrix[(N - 1) - index][i + index] = value[i]
    index += 1

for value in matrix:
    print(''.join(value))
