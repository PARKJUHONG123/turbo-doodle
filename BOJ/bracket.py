import sys

T = int(sys.stdin.readline())
MOD = 1000000007
max_L = 5000
dp = [0 for _ in range(max_L + 1)]
ap = [0 for _ in range(max_L + 1)]

dp[2], ap[2] = 1, 1

for i in range(4, max_L + 1, 2):
    dp[i] = ap[i - 2]
    tmp = 0
    for j in range(2, i, 2):
        tmp = (tmp + ap[j] * dp[i - j]) % MOD
    ap[i] = (ap[i] + dp[i] + tmp) % MOD

for _ in range(T):
    L = int(sys.stdin.readline())
    print(ap[L])