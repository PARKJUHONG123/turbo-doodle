n = int(input())
t = [0 for _ in range(n)]
p = [0 for _ in range(n)]

dp = [0 for _ in range(n + 1)]

for i in range(n):
    temp = input()
    temp = temp.split()
    t[i], p[i] = int(temp[0]), int(temp[1])

for i in range(n):
    if t[i] + i <= n and dp[i] + p[i] > dp[t[i] + i] :
        dp[t[i] + i] = dp[i] + p[i]
        for j in range(t[i] + i, n):
            if (dp[j] < dp[t[i] + i]):
                dp[j] = dp[t[i] + i]

print(max(dp))
