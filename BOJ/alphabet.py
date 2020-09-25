import sys

R, C = list(map(int, sys.stdin.readline().split()))
matrix = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]

a_value = ord('A')
alpha_length = ord('Z') - ord('A') + 1
alpha_visited = [False for _ in range(alpha_length)]
max_count = 0

x_dir = [-1, 1, 0, 0]
y_dir = [0, 0, -1, 1]

def to_num(x, y):
    return ord(matrix[x][y]) - a_value

def dfs(x, y, count):
    global max_count

    if count == alpha_length:
        print(count)
        exit()
    else:
        max_count = max(max_count, count)

    for i in range(4):
        dx, dy = x + x_dir[i], y + y_dir[i]
        if 0 <= dx < R and 0 <= dy < C:
            beta = to_num(dx, dy)
            if not alpha_visited[beta]:
                alpha_visited[beta] = True
                dfs(dx, dy, count + 1)
                alpha_visited[beta] = False

alpha_visited[to_num(0, 0)] = True
dfs(0, 0, 1)
print(max_count)