import sys
from itertools import combinations

N = int(sys.stdin.readline().split()[0])
matrix = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        matrix[i][j] = tmp[j]

M = [i for i in range(0, N)]
comb_list = combinations(M, N // 2)

dictionary = dict()
comb_list = list(comb_list)

for value in comb_list:
    total = 0
    for a in value:
        for b in value:
            total += matrix[a][b]
    dictionary[value] = total

length = len(comb_list)
min_distance = 98765321
for i in range(length // 2):
    min_distance = min(min_distance, abs(dictionary[comb_list[i]] - dictionary[comb_list[length - i - 1]]))
print(min_distance)
