import sys
N = int(sys.stdin.readline())
value = list(map(int, sys.stdin.readline().split()))

def brute(index, value, visited, total):
    if not (False in visited):
        return total
    ret = 0
    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            ret = max(ret, brute(i, value, visited, total + abs(value[i] - value[index])))
            visited[i] = False
    return ret

ret = 0
visited = [False for _ in range(N)]
for i in range(N):
    visited[i] = True
    ret = max(ret, brute(i, value, visited, 0))
    visited[i] = False

print(ret)