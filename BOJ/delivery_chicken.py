import sys
import math
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())
matrix = [[] for _ in range(N)]

chicken_list = []
house_list = []
for i in range(N):
    matrix[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if matrix[i][j] == 1:
            house_list.append([i, j])
        elif matrix[i][j] == 2:
            chicken_list.append([i, j])

remained_chicken = combinations(chicken_list, M)

min_length = math.inf
for real_chicken in remained_chicken:
    total_length = 0
    for house in house_list:
        house_x, house_y = house
        length = math.inf
        for chicken in real_chicken:
            chicken_x, chicken_y = chicken
            length = min(abs(house_x - chicken_x) + abs(house_y - chicken_y), length)
        total_length += length
    min_length = min(min_length, total_length)
print(min_length)