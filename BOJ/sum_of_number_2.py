import sys
N, M = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
count = 0
total = arr[start]

while True:
    if start <= end < N:
        if total == M:
            count += 1
            end += 1
            if end < N:
                total += arr[end]
        elif total < M:
            end += 1
            if end < N:
                total += arr[end]
        elif total > M:
            total -= arr[start]
            start += 1
    else:
        if end < start <= N:
            end += 1
            if end < N:
                total += arr[end]
            continue
        if end == N:
            if start == N:
                break
            else:
                while start < N:
                    total -= arr[start]
                    if total == M:
                        count += 1
                    start += 1
print(count)
'''
dp = [[0 for _ in range(i + 1)] for i in range(N)]
over_M = 0
for i in range(N):
    result = arr[i]
    dp[i][i] = result
    if result == M:
        answer += 1
    elif result > M:
        over_M += 1

if over_M == N:
    print(answer)
    exit()

for k in range(1, N):
    over_M = 0
    for i in range(N - k):
        j = i + k
        result = dp[j - 1][i] + dp[j][j]
        dp[j][i] = result
        if result == M:
            answer += 1
        elif result > M:
            over_M += 1
    if over_M == N - k:
        break

print(answer)
'''