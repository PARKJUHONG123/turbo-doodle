import sys

k = int(sys.stdin.readline())
signs = sys.stdin.readline().split()
num = [i for i in range(10)]
visited = [False for _ in range(10)]

rets = []

def brute(visited, index, last, ret):
    if index == k + 1:
        rets.append(ret)
        return

    if index > 0:
        if signs[index - 1] == '<':
            for value in range(10):
                if last < value and not visited[value]:
                    visited[value] = True
                    brute(visited, index + 1, value, ret + str(value))
                    visited[value] = False
        else:
            for value in range(10):
                if last > value and not visited[value]:
                    visited[value] = True
                    brute(visited, index + 1, value, ret + str(value))
                    visited[value] = False
    else:
        for value in range(10):
            if not visited[value]:
                visited[value] = True
                brute(visited, index + 1, value, ret + str(value))
                visited[value] = False

brute(visited, 0, -1, "")
rets.sort()
print(rets[-1])
print(rets[0])
