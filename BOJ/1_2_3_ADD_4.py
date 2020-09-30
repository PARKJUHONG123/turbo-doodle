import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    if N == 1:
        print(1)
    elif N == 2:
        print(2)
    elif N == 3:
        print(3)
    else:
        dp = [[0, 0, 0] for _ in range(N + 1)]
        dp[1], dp[2], dp[3] = [1, 0, 0], [1, 1, 0], [1, 1, 1]
        for i in range(4, N + 1):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = dp[i - 2][0] + dp[i - 2][1]
            dp[i][2] = dp[i - 3][0] + dp[i - 3][1] + dp[i - 3][2]
        print(sum(dp[N]))
