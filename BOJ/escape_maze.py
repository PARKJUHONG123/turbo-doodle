import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, sys.stdin.readline().split())
graph_list = []
for _ in range(N):
    graph_list.append(list(map(int, str(input()))))


def bfs_deque(graph_list, root_i, root_j, M, N):
    visited = []
    queue = deque([[root_i, root_j]])
    distance = [[0 for _ in range(M)] for _ in range(N)]
    distance[root_i][root_j] = 1

    while queue:
        [i, j] = queue.popleft()
        visited.append([i, j])
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if graph_list[nx][ny] == 1 and [nx, ny] not in visited and [nx, ny] not in queue:
                    queue.append([nx, ny])
                    distance[nx][ny] = distance[i][j] + 1
    return distance[-1][-1]


def dfs_deque(graph_list, root_i, root_j, M, N):
    visited = []
    stack = deque([[root_i, root_j]])
    distance = [[0 for _ in range(M)] for _ in range(N)]
    distance[root_i][root_j] = 1

    while stack:
        [i, j] = stack.pop()
        visited.append([i, j])
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if graph_list[nx, ny] == 1 and [nx, ny] not in visited and [nx, ny] not in stack:
                    stack.append([nx, ny])
                    distance[nx, ny] = distance[i][j] + 1
    return distance[-1][-1]


def bfs_self(graph_list, root_i, root_j, M, N):
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
                if graph_list[nx][ny] == 1 and [nx, ny] not in visited:
                    queue.append([nx, ny])
                    distance[nx][ny] = distance[i][j] + 1
    return distance[-1][-1]


def dfs_self(graph_list, root_i, root_j, M, N):
    visited = []
    stack = [[root_i, root_j]]
    distance = [[0 for _ in range(M)] for _ in range(N)]
    distance[root_i][root_j] = 1

    while stack:
        [i, j] = stack.pop()
        visited.append([i, j])
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if graph_list[nx][ny] == 1 and [nx, ny] not in visited and [nx, ny] not in stack:
                    stack.append([nx, ny])
                    distance[nx][ny] = distance[i][j] + 1
    return distance[-1][-1]

print(bfs_deque(graph_list, 0, 0, M, N))