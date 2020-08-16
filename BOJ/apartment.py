import sys
from collections import deque

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

N = int(sys.stdin.readline())

n_arr = [[0 for _ in range(N)] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    temp = sys.stdin.readline()
    for j in range(N):
        n_arr[i][j] = int(temp[j])

def bfs(x, y, team):
    if visited[x][y] != 0 or n_arr[x][y] == 0:
        return -1

    dq = deque()
    dq.append([x, y])
    visited[x][y] = team

    while(dq):
        temp = dq.popleft()
        if n_arr[temp[0]][temp[1]] == 1 :
            for i in range(4):
                dx = temp[0] + direction[i][0]
                dy = temp[1] + direction[i][1]
                if 0 <= dx < N and 0 <= dy < N:
                    if visited[dx][dy] == 0 and n_arr[dx][dy] == 1:
                        dq.append([dx, dy])
                        visited[dx][dy] = team
    return team + 1

team = 1
for i in range(N):
    for j in range(N):
        get_team = bfs(i, j, team)
        if get_team != -1:
            team = get_team

d_arr = [0 for _ in range(team)]

for i in range(N):
    for j in range(N):
        d_arr[visited[i][j]] += 1

del(d_arr[0])
d_arr.sort()

team = team - 1
print(team)
for i in range(team):
    print(d_arr[i])