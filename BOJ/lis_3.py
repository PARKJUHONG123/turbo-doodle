import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def lower_bound(arr, target):
    start, end = 0, len(arr) - 1

    while end > start:
        mid = (end + start) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return end

ret = []
for value in arr:
    if not ret:
        ret.append(value)
    else:
        if ret[-1] < value:
            ret.append(value)
        else:
            ret[lower_bound(ret, value)] = value
print(len(ret))
