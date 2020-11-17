import sys

N, K = map(int, sys.stdin.readline().split())
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

max_value = -sys.maxsize
for i in range(1, N + 1):
    W, V = map(int, sys.stdin.readline().split())
    for j in range(K + 1):
        if j >= W:
            dp[i][j] = max(dp[i - 1][j - W] + V, dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
    max_value = max(max_value, max(dp[i]))

print(max_value)