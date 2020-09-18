import sys
from itertools import permutations
INF = 987654321
N = int(sys.stdin.readline())

lst = [i for i in range(N)]

matrix = [[INF for _ in range(N)] for _ in range(N)]
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if tmp[j]:
            matrix[i][j] = tmp[j]

max_value = INF
for value in list(permutations(lst, N)):
    ret = 0
    for i in range(len(value) - 1):
        ret += matrix[value[i]][value[i + 1]]
    ret += matrix[value[-1]][value[0]]
    if max_value > ret:
        max_value = ret
print(max_value)
