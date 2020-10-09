from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
arr = [[0 for j in range(M)] for i in range(N)]
copy_ = [[0 for j in range(M)] for i in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

answer =0

for i in range(N):
    row_input = list(map(int,input().split()))
    for j in range(M):
        arr[i][j] = row_input[j]

combi_list = []
virus_list = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 :
            combi_list.append([i,j])
        elif arr[i][j] == 2 :
            virus_list.append([i,j])

blocks = list(combinations(combi_list,3))

def bfs():
    global copy_
    global answer
    visit = [[0 for j in range(M)] for i in range(N)]
    dq = deque()
    sum = 0
    for virus in virus_list :
        dq.append([virus[0],virus[1]])
        visit[virus[0]][virus[1]] = 1

    while dq :
        virus = dq.popleft()
        x, y = virus[0], virus[1]

        for j in range(0,4):
            next_x = x + dx[j]
            next_y = y + dy[j]

            if next_x < 0 or next_y < 0 or next_x > N-1 or next_y > M-1 :
                continue
            if copy_[next_x][next_y] == 1 or copy_[next_x][next_y] == 2:
                continue
            if visit[next_x][next_y] == 1:
                continue

            copy_[next_x][next_y] = 2
            dq.append([next_x,next_y])
            visit[next_x][next_y] = 1


    for i in range(0,N):
        for j in range(0,M):
            if copy_[i][j] == 0 :
                sum+=1

    if answer < sum :
        answer = sum


for block in blocks :
    for wall in block :
        arr[wall[0]][wall[1]] = 1

    copy_ = copy.deepcopy(arr)
    bfs()

    for wall in block :
        arr[wall[0]][wall[1]] = 0

print(answer)