import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(N)]
arr = [[i] for i in A]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            if dp[j] + 1 > dp[i]:
                arr[i] = arr[j] + [A[i]]
                dp[i] = dp[j] + 1
length = 0
flag = 0
for i in range(N):
    if length < dp[i]:
        flag = i
        length = dp[i]

print(length)
print(*arr[flag])