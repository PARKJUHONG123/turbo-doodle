import sys

N, M = map(int, sys.stdin.readline().split())
guitar_lesson = list(map(int, sys.stdin.readline().split()))
low, high = 0, sum(guitar_lesson)


def able_blueray(standard):
    count = 1
    stack = 0
    for i in range(N):
        if guitar_lesson[i] > standard:
            return False
        if stack + guitar_lesson[i] > standard:
            count += 1
            if count > M:
                return False
            stack = guitar_lesson[i]
        else:
            stack += guitar_lesson[i]
    return True

while low <= high:
    mid = (low + high) // 2
    if able_blueray(mid):
        high = mid - 1
    else:
        low = mid + 1

print(low)
