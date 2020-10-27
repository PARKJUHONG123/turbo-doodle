import sys
import math
N = int(sys.stdin.readline())
matrix = [[] for _ in range(N)]
INF = math.inf
for i in range(N):
    matrix[i] = list(map(int, sys.stdin.readline().split()))

all_visited = (1 << N) - 1
dp = [[0 for _ in range(1 << N)] for _ in range(N)]

def TSP(cur_index, visited):
    if visited == all_visited:
        return (matrix[cur_index][0] if matrix[cur_index][0] > 0 else INF)
    if dp[cur_index][visited] > 0:
        return dp[cur_index][visited]

    answer = INF
    for i in range(1, N):
        if (visited >> i) % 2 == 1 or matrix[cur_index][i] == 0:
            continue
        answer = min(answer, matrix[cur_index][i] + TSP(i, visited | (1 << i)))
    dp[cur_index][visited] = answer
    return answer

print(TSP(0, 1))