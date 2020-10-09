import sys
from itertools import combinations

N, M, H = map(int, sys.stdin.readline().split())

bridge = [[] for _ in range(H)]
visited = [[False for _ in range(N)] for _ in range(H)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    bridge[a - 1].append([b - 1, b])
    visited[a - 1][b - 1] = True

not_visited = []
for i in range(H):
    for j in range(N):
        if not visited[i][j]:
            if j == 0:
                if j + 1 < N:
                    if not visited[i][j + 1]:
                        not_visited.append((i, j))
            elif j == N - 1:
                if j - 1 >= 0:
                    if not visited[i][j - 1]:
                        not_visited.append((i, j))
            else:
                if j - 1 >= 0 and j + 1 < N:
                    if not visited[i][j - 1] and not visited[i][j + 1]:
                        not_visited.append((i, j))

def go_ladder():
    for start_y in range(N):
        y = start_y
        for x in range(H):
            if y == 0:
                if visited[x][y]:
                    y = y + 1
            elif y == N - 1:
                if y - 1 >= 0:
                    if visited[x][y - 1]:
                        y = y - 1
            else:
                if y - 1 >= 0 and y < N:
                    if visited[x][y - 1] and visited[x][y]:
                        return False
                    else:
                        if visited[x][y - 1]:
                            y = y - 1
                        elif visited[x][y]:
                            y = y + 1
        if y == start_y:
            pass
        else:
            return False
    return True

for i in range(4):
    for value in combinations(not_visited, i):
        for element in value:
            visited[element[0]][element[1]] = True

        if go_ladder():
            print(i)
            exit()

        for element in value:
            visited[element[0]][element[1]] = False
print(-1)