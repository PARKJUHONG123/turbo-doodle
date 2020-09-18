from itertools import permutations
import sys

N = int(sys.stdin.readline())
lst = [(i + 1) for i in range(N)]

value = list(permutations(lst, N))
for element in value:
    element = list(element)
    print(' '.join(list(map(str, element))))
