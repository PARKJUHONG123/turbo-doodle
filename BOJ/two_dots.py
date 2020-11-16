import sys

dir_x = [-1, 0, 0, 1]
dir_y = [0, -1, 1, 0]

N, M = map(int, sys.stdin.readline().split())
matrix = [list() for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

alpha_dict = dict()
for i in range(N):
    temp = sys.stdin.readline().strip()
    for j in range(M):
        alpha = temp[j]
        if alpha in alpha_dict:
            alpha_dict[alpha] += 1
        else:
            alpha_dict[alpha] = 1
        matrix[i].append(alpha)

def search_start():
    for i in range(N):
        if False in visited[i]:
            return [i, visited[i].index(False)]
    return [-1, -1]

def dfs(index, alpha, count_huddle):
    x, y = index
    stack = list()
    stack.append([x, y, 1])
    visited[x][y] = True

    while stack:
        tx, ty, count = stack.pop()
        for i in range(4):
            dx, dy = tx + dir_x[i], ty + dir_y[i]
            if 0 <= dx < N and 0 <= dy < M:
                if matrix[dx][dy] == alpha:
                    if count >= 4:
                        return True
                    if count + 1 <= count_huddle:
                        stack.append([dx, dy, count + 1])
    return False

while True:
    index = search_start()
    if index == [-1, -1]:
        break
    alpha = matrix[index[0]][index[1]]
    if dfs(index, alpha, alpha_dict[alpha]):
        print("Yes")
        exit()
print("No")


