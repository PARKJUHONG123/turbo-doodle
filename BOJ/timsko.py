import sys
N, M, K = map(int, sys.stdin.readline().split())

max_team = 0
for i in range(K + 1):
    n_left, m_left = N - i, M - (K - i)
    max_team = max(max_team, min(n_left // 2, m_left))
print(max_team)