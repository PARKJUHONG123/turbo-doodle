import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(N + 1)]

tmp = list(map(int, sys.stdin.readline().split()))
for i in range(1, N + 1):
    dp[i] = tmp[i - 1]

for i in range(1, N + 1):
    for a in range(1, i):
        b = i - a
        if b > a:
            continue
        dp[i] = min(dp[i], dp[a] + dp[b])

print(dp[-1])