import sys
from itertools import combinations

N = int(sys.stdin.readline())
players = set([i for i in range(N)])

dp = [[0 for _ in range(N)] for _ in range(N)]
matrix = [[] for _ in range(N)]
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    matrix[i] = tmp

for i in range(N):
    for j in range(N):
        dp[i][j] = matrix[i][j] + matrix[j][i]

min_point = 987654321
for i in range(1, N // 2 + 1):
    for a_side in combinations(players, i):
        a_point, b_point = 0, 0
        if len(a_side) > 1:
            for two_players in combinations(a_side, 2):
                a_point += dp[two_players[0]][two_players[1]]

        b_side = players - set(a_side)
        if len(b_side) > 1:
            for two_players in combinations(b_side, 2):
                b_point += dp[two_players[0]][two_players[1]]
        min_point = min(abs(a_point - b_point), min_point)
print(min_point)
