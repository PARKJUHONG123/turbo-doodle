import sys
from itertools import permutations

n, m = list(map(int, sys.stdin.readline().split()))
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

comb_lst = list(permutations(lst, m))
for value in comb_lst:
    value = list(map(str, value))
    print(' '.join(value))