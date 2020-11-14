import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
start, end = 0, max(arr)

def left_tree(arr, height):
    ret = 0
    for value in arr:
        ret += (value - height if value >= height else 0)
    return ret

while start <= end:
    mid = (start + end) // 2
    if M <= left_tree(arr, mid):
        start = mid + 1
    else:
        end = mid - 1
print(end)