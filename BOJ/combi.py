import sys

N, M = map(int, sys.stdin.readline().split())

def comb(n, m):
    up, under = 1, 1
    for i in range(1, m + 1):
        under *= i
        up *= (n - (i - 1))
    return up // under

if N - M < M:
    print(comb(N, N - M))
else:
    print(comb(N, M))