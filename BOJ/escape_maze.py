import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, sys.stdin.readline().split())
graph_list = []
for _ in range(N):
    graph_list.append(list(map(int, str(input()))))

def bfs(graph_list, root_i, root_j, M, N):
    visited = []
    queue = [[root_i, root_j]]
    distance = [[0 for _ in range(M)] for _ in range(N)]
    distance[root_i][root_j] = 1

    while queue:
        [i, j] = queue.pop(0)
        visited.append([i, j])
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if graph_list[nx][ny] == 1 :
                    if not [nx, ny] in visited:
                        queue.append([nx, ny])
                        distance[nx][ny] = distance[i][j] + 1

    return distance[N - 1][M - 1]

print(bfs(graph_list, 0, 0, M, N))
