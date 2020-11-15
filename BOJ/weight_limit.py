import sys
N, M = map(int, sys.stdin.readline().split())
cities = dict()
MAX_VALUE = -1

def insert_cities(A, B, C):
    global MAX_VALUE
    if A in cities:
        if B in cities[A]:
            cities[A][B] = max(cities[A][B], C)
        else:
            cities[A][B] = C
    else:
        cities[A] = dict()
        cities[A][B] = C
    MAX_VALUE = max(MAX_VALUE, cities[A][B])

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    insert_cities(A, B, C)
    insert_cities(B, A, C)

start, end = map(int, sys.stdin.readline().split())

def dfs(cost):
    stack = list()
    stack.append(start)
    visited = [False for _ in range(N + 1)]
    visited[start] = True

    while stack:
        cur = stack.pop()
        if cur == end:
            return True
        else:
            for key in cities[cur].keys():
                if not visited[key] and cost <= cities[cur][key]:
                    visited[key] = True
                    stack.append(key)
    return False

if start == end:
    print(0)
else:
    low, high = 0, MAX_VALUE
    while low <= high:
        mid = (low + high) // 2
        if dfs(mid):
            low = mid + 1
        else:
            high = mid - 1
    print(high)