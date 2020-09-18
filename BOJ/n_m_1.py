import sys
from itertools import combinations

n, m = list(map(int, sys.stdin.readline().split()))
lst = [str(i) for i in range(1, n + 1)]

for value in list(combinations(lst, m)):
    print(" ".join(value))