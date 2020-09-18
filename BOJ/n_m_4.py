import sys
n, m = list(map(int, sys.stdin.readline().split()))

lst = [i + 1 for i in range(n)]

def brute(lst, index, last_index, str_value):
    if index == m:
        print(str_value[:-1])
        return
    for i in range(last_index, n):
        brute(lst, index + 1, i, str_value + str(lst[i]) + " ")

brute(lst, 0, 0, "")
