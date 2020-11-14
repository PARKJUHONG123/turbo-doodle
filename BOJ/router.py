import sys

N, M = map(int, sys.stdin.readline().split())
arr = list()
for _ in range(N):
    arr.append(int(sys.stdin.readline().strip()))
arr.sort()

left = 1
right = arr[-1] - arr[0]

while left <= right:
    mid = (left + right) // 2
    start = arr[0]
    count = 1

    for i in range(1, N):
        distance = arr[i] - start
        if mid <= distance:
            count += 1
            start = arr[i]

    if count >= M:
        left = mid + 1
    else:
        right = mid - 1
print(right)