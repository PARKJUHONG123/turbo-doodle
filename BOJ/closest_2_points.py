import sys

def dist(X, Y):
    return (X[0] - Y[0]) ** 2 + (X[1] - Y[1]) ** 2

def calc(left, right):
    if right - left == 1:
        return dist(arr[left], arr[right])
    elif right - left == 2:
        return min(min(dist(arr[left], arr[right]), dist(arr[left], arr[right - 1])), dist(arr[left + 1], arr[right]))
    mid = (left + right) // 2
    distance = min(calc(left, mid), calc(mid + 1, right))

    drr = []
    for i in range(left, right + 1):
        x_dist = (arr[i][0] - arr[mid][0]) ** 2
        if x_dist >= distance:
            continue
        drr.append(arr[i])
    drr.sort(key = lambda x : x[1])
    drr_length = len(drr)

    for i in range(drr_length - 1):
        for j in range(i + 1, drr_length):
            y_dist = (drr[i][1] - drr[j][1]) ** 2
            if y_dist >= distance:
                break
            x_dist = (drr[i][0] - drr[j][0]) ** 2
            distance = min(distance, x_dist + y_dist)
    return distance

N = int(sys.stdin.readline().strip())
arr = [[] for _ in range(N)]
arr_dict = dict()

for i in range(N):
    value = tuple(map(int, sys.stdin.readline().split()))
    if value in arr_dict:
        print(0)
        exit()
    else:
        arr_dict[value] = True
        arr[i] = value
arr.sort()
print(calc(0, N - 1))