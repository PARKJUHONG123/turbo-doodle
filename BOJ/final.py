temp = input()
temp = temp.split()
M = int(temp[0])
N = int(temp[1])

visited = [[False for _ in range(N)] for _ in range(M)]
arrow = [[-1, 0], [+1, 0], [0, -1], [0, +1]]
d_arr = [[0 for _ in range(N)] for _ in range(M)]
visited[0][0] = True

def dfs(start_x, start_y, end_x, end_y, visited):
    if start_x == end_x and start_y == end_y:
        false_in = False
        for k in range(M):
            if False in visited[k]:
                false_in = True
                break

        if false_in == False:
            d_arr[end_x][end_y] += 1

    for i in range(4):
        dx = start_x + arrow[i][0]
        dy = start_y + arrow[i][1]
        if 0 <= dx < M and 0 <= dy < N :
            if visited[dx][dy] == False:
                visited[dx][dy] = True
                dfs(dx, dy, end_x, end_y, visited)
                visited[dx][dy] = False

dfs(0, 0, M - 1, 0, visited)
print(d_arr[M - 1][0])