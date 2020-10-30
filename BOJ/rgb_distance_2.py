import sys

N = int(sys.stdin.readline().strip())
color = [[0 for _ in range(3)] for _ in range(N)]

# R : 0, G : 1, B : 2
for i in range(N):
    color[i][0], color[i][1], color[i][2] = map(int, sys.stdin.readline().split())

dp = [[0 for _ in range(3)] for _ in range(N)]
INF = 987654321
answer = INF

for k in range(3):
    for i in range(3):
        if i == k:
            dp[0][i] = color[0][i]
        else:
            dp[0][i] = 987654321

    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + color[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + color[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + color[i][2]

    for i in range(3):
        if i != k:
            answer = min(answer, dp[N - 1][i])
print(answer)