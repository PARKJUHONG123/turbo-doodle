import sys

def count_line(arr, length):
    ret = 0
    for value in arr:
        ret += (value // length)
    return ret

K, N = map(int, sys.stdin.readline().split())
arr = list()
for _ in range(K):
    arr.append(int(sys.stdin.readline().strip()))

start = 1
end = max(arr)
dp_dict = dict()

while start <= end:
    mid = (start + end) // 2
    if mid in dp_dict:
        count = dp_dict[mid]
    else:
        dp_dict[mid] = count_line(arr, mid)
        count = dp_dict[mid]

    if N > count: # 더 얇아져야 함
        end = mid - 1
    else:
        start = mid + 1
print(end)