import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
low, high = 0, max(arr)


def sum_part(standard):
    count = 1
    inner_min, inner_max = arr[0], arr[0]
    for i in range(N):
        inner_min = min(inner_min, arr[i])
        inner_max = max(inner_max, arr[i])
        if inner_max - inner_min > standard:
            count += 1
            if count > M:
                return False
            inner_min, inner_max = arr[i], arr[i]
    return True


while low <= high:
    mid = (low + high) // 2
    if not sum_part(mid):
        low = mid + 1
    else:
        high = mid - 1
print(low)