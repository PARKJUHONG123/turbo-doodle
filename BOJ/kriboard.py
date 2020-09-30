import sys

N = int(sys.stdin.readline())

dp = [i for i in range(N + 1)]

if N == 1:
    print(1)
    exit()
elif N == 2:
    print(2)
    exit()
elif N == 3:
    print(3)
    exit()
else:
    for i in range(4, N + 1):
        for j in range(1, i - 2):
            dp[i] = max(dp[j] * (i - j - 1), dp[i])

print(dp[-1])
