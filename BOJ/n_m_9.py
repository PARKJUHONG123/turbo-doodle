import sys
from itertools import permutations

n, m = list(map(int, sys.stdin.readline().split()))
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

comb_lst = list(permutations(lst, m))
comb_lst = list(set(comb_lst))
comb_lst.sort()
for value in comb_lst:
    value = list(map(str, value))
    print(' '.join(value))