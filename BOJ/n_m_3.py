import sys
n, m = list(map(int, sys.stdin.readline().split()))

lst = [i + 1 for i in range(n)]

def brute(lst, index, str_value):
    if index == m:
        print(str_value[:-1])
        return
    for i in range(n):
        brute(lst, index + 1, str_value + str(lst[i]) + " ")

brute(lst, 0, "")
