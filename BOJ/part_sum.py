import sys
N, M = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
length = 987654321
total = arr[start]

while True:
    if start <= end < N:
        if total == M:
            length = min(end + 1 - start, length)
            end += 1
            if end < N:
                total += arr[end]
        elif total < M:
            end += 1
            if end < N:
                total += arr[end]
        elif total > M:
            length = min(end + 1 - start, length)
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
                    if total >= M:
                        length = min(end + 1 - start, length)
                    start += 1
if length == 987654321:
    print(0)
else:
    print(length)
