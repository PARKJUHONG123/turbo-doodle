import sys
N = int(sys.stdin.readline().strip())
L = list(map(int, sys.stdin.readline().split()))
P = [0 for _ in range(N)]
count = 0

def merge(L, left, mid, right):
    global count
    i, j, k = left, mid + 1, left
    while i <= mid and j <= right:
        if L[i] <= L[j]:
            P[k] = L[i]
            i += 1
        else:
            P[k] = L[j]
            j += 1
            count += (mid + 1 - i)
        k += 1

    if mid < i:
        for l in range(j, right + 1):
            P[k] = L[l]
            k += 1
    else:
        for l in range(i, mid + 1):
            P[k] = L[l]
            k += 1
    for l in range(left, right + 1):
        L[l] = P[l]

def merge_sort(L, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(L, left, mid)
        merge_sort(L, mid + 1, right)
        merge(L, left, mid, right)

merge_sort(L, 0, N - 1)
print(count)