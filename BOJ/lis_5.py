import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def lower_bound(arr, target):
    start, end = 0, len(arr) - 1

    while end > start:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return end

ret = []
p = [1 for _ in range(len(arr))]
for i in range(len(arr)):
    value = arr[i]
    if not ret:
        ret.append(value)
        p[i] = 1
    else:
        if ret[-1] < value:
            ret.append(value)
            p[i] = len(ret)
        else:
            index = lower_bound(ret, value)
            ret[index] = value
            p[i] = index + 1

def backtrace(p_index):
    ret = []
    for i in reversed(range(len(arr))):
        if p_index == 0:
            return ret
        if p_index == p[i]:
            ret = [arr[i]] + ret
            p_index -= 1
    return ret

p_index = max(p)
print(p_index)
backtrace_ret = backtrace(p_index)
print(*backtrace_ret)
