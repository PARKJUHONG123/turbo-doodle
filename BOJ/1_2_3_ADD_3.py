import sys
MOD = 1000000009
T = int(sys.stdin.readline())

N = 1000001
dp = [0 for _ in range(N)]
dp[0], dp[1], dp[2] = 1, 2, 4

for i in range(3, N):
    dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % MOD

for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp[n - 1])