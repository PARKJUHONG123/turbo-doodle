import sys

arr = sys.stdin.readline().strip()
length = len(arr)
dp = [[0 for _ in range(length)] for _ in range(length)]

for i in range(length):
    dp[i][i] = 1
    if i + 1 < length:
        if arr[i] == arr[i + 1]:
            dp[i][i + 1] = 1
        if i - 1 >= 0:
            if arr[i - 1] == arr[i + 1]:
                dp[i - 1][i + 1] = 1

for j in range(2, length):
    for i in range(length):
        if i + j < length:
            if arr[i] == arr[i + j] and dp[i + 1][i + j - 1]:
                dp[i][i + j] = 1
            if i - j >= 0:
                if arr[i - j] == arr[i + j] and dp[i - j + 1][i + j - 1]:
                    dp[i - j][i + j] = 1

ret = [0 for _ in range(length)]
for i in range(length):
    for j in range(i + 1):
        if dp[j][i]:
            if ret[i] == 0 or ret[i] > ret[j - 1] + 1:
                ret[i] = ret[j - 1] + 1

print(ret[-1])
