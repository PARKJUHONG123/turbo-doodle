import sys

n, k = map(int, sys.stdin.readline().split())
dp = [0 for _ in range(k + 1)]
dp[0] = 1
coin_list = []
for _ in range(n):
    coin = int(sys.stdin.readline())
    if coin <= k:
        coin_list.append(coin)
coin_list.sort()
for value in coin_list:
    for i in range(k + 1):
        if i - value >= 0:
            dp[i] += dp[i - value]
print(dp[-1])