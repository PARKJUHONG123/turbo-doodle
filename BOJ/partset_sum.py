from itertools import combinations
import sys

N, S = list(map(int, sys.stdin.readline().split()))
lst = list(map(int, sys.stdin.readline().split()))

count = 0
for i in range(1, N + 1):
    comb_lst = combinations(lst, i)
    for value in comb_lst:
        if sum(value) == S:
            count += 1
print(count)