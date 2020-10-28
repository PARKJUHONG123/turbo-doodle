def bubble_sort(arr):
    # time = O(n^2)
    # space = O(n)
    # In-place Sort (다른 메모리 공간 필요 X length 안에서만 해결 가능)
    # Stable Sort (같은 값의 순서가 바뀌지 않음)

    length = len(arr)
    for i in range(length):
        for j in range(1, length - i):
            if arr[j - 1] > arr[j]:
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp
    print(arr)


def selection_sort(arr):
    # time = O(n^2)
    # space = O(n)
    # In-place Sort
    # Unstable Sort (같은 값의 순서가 바뀜)
    # [5(1), 4, 5(2), 2] -> [2, 4, 5(2), 5(1)]

    length = len(arr)
    for i in range(length - 1):
        start_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[start_index]:
                start_index = j
        temp = arr[start_index]
        arr[start_index] = arr[i]
        arr[i] = temp
    print(arr)


def insertion_sort(arr):
    # worst & ave time = O(n^2)
    # best time = O(n)
    # space = O(n)
    # In-place Sort
    # Stable Sort

    length = len(arr)
    for i in range(length):
        temp = arr[i]
        prev = i - 1
        while prev >= 0 and arr[prev] > temp:
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = temp
    print(arr)


def partition(arr, left, right):
    pivot = arr[left]
    i, j = left, right

    while i < j:
        while pivot < arr[j]:
            j -= 1
        while i < j and pivot >= arr[i]:
            i += 1
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    arr[left] = arr[i]
    arr[i] = pivot
    return i

def quick_sort(arr, left, right):
    # JAVA : Arrays.sort() Java 7부터 Dual Pivot Quick Sort
    # worst time = O(n^2)
    # ave & best time = O(n * log(n))
    # space = O(n)
    # In-place Sort
    # Unstable Sort

    if left >= right:
        return
    pivot = partition(arr, left, right)
    quick_sort(arr, left, pivot)
    quick_sort(arr, pivot + 1, right)


def merge(arr, left, mid, right):
    L, R = arr[left : mid + 1], arr[mid + 1 : right + 1]
    l_length, r_length = len(L), len(R)
    i, j, k = 0, 0, left

    while i < l_length and j < r_length:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < l_length:
        arr[k] = L[i]
        k, i = k + 1, i + 1
    while j < r_length:
        arr[k] = R[j]
        k, j = k + 1, j + 1

def merge_sort(arr, left, right):
    # time : O(n * log(n))
    # Not In-Place Sort
    # Stable Sort

    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def heapify(arr, length, i):
    parent, left, right = i, i * 2 + 1, i * 2 + 2

    if left < length and arr[parent] < arr[left]:
        parent = left
    if right < length and arr[parent] < arr[right]:
        parent = right
    if i != parent:
        temp = arr[parent]
        arr[parent] = arr[i]
        arr[i] = temp
        heapify(arr, length, parent)

def heap_sort(arr):
    # time : O(n * log(n))
    # Unstable Sort
    length = len(arr)

    for i in reversed(range(length // 2)):
        heapify(arr, length, i)
    for i in reversed(range(length)):
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        heapify(arr, i, 0)
    print(arr)


def count_sort(arr, n, exp):
    buffer = [0 for _ in range(n)]
    count = [0 for _ in range(10)]

    for i in range(n):
        count[(arr[i] // exp) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in reversed(range(n)):
        index = (arr[i] // exp) % 10
        buffer[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = buffer[i]

def radix_sort(arr):
    length = len(arr)
    m = max(arr)
    exp = 1
    while m / exp > 0:
        count_sort(arr, length, exp)
        exp *= 10
    print(arr)


bubble_sort([3, 2, 4, 7, 5, 1])
selection_sort([3, 2, 4, 7, 5, 1])
insertion_sort([3, 2, 4, 7, 5, 1])

arr = [3, 2, 4, 7, 5, 1]
quick_sort(arr, 0, 5)
print(arr)

arr = [3, 2, 4, 7, 5, 1]
merge_sort(arr, 0, 5)
print(arr)

heap_sort([3, 2, 4, 7, 5, 1])
radix_sort([3, 2, 4, 3, 7, 5, 1])