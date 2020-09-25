import sys

T = int(sys.stdin.readline())
MOD = 1000000009

dp = [[0 for _ in range(4)] for _ in range(100001)]

dp[1][1], dp[1][2], dp[1][3] = 1, 0, 0
dp[2][1], dp[2][2], dp[2][3] = 0, 1, 0
dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1

for i in range(4, 100001):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % MOD
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % MOD

for _ in range(T):
    n = int(sys.stdin.readline())
    ret = 0
    for i in range(1, 4):
        ret += dp[n][i]
        ret %= MOD
    print(ret)
