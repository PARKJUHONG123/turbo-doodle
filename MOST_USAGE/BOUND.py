def lower_bound(arr, target):
    start, end = 0, len(arr) - 1

    while end > start:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return end

def upper_bound(arr, target):
    start, end = 0, len(arr) - 1

    while end > start:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid
        else:
            start = mid + 1
    return end

print(lower_bound([1, 3, 4, 5, 7, 9, 12, 13, 15, 18], 3)) # 몇번 째 인덱스부터 3 이상이 되는지
print(upper_bound([1, 3, 4, 5, 7, 9, 12, 13, 15, 18], 3)) # 몇번 째 인덱스부터 3 초과가 되는지

arr = [3, 2, 5, 2, 3, 1, 4]
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

def backtrace(index):
    ret = []
    for i in reversed(range(len(arr))):
        if index == 0:
            return ret
        if p[i] == index:
            ret = [arr[i]] + ret
            index -= 1

print(backtrace(max(p)))
print(p)
