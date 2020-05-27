temp = input()
temp = temp.split()

N = int(temp[0])
M = int(temp[1])

if (N < M) :
    temp = N
    N = M
    M = temp

# N > M

dp = [0 for _ in range(M + 1)]

for i in range(1, M + 1):
    if i == 1 :
        dp[i] = N - 1
    else :
        max_value = 0
        for j in range(i):
            if max_value < 1 + dp[j] + dp[i - j]:
                max_value = 1 + dp[j] + dp[i - j]
        dp[i] = max_value

print(dp[-1])