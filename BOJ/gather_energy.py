import sys

N = int(sys.stdin.readline())
visited = [False for _ in range(N)]
power_list = list(map(int, sys.stdin.readline().split()))

def very_left(index, visited):
    for i in reversed(range(index)):
        if not visited[i]:
            return i
    return -1

def very_right(index, visited):
    for i in range(index + 1, N):
        if not visited[i]:
            return i
    return -1

max_power = 0
def brute(visited, power, count):
    if count == N - 2:
        global max_power
        max_power = max(max_power, power)

    for i in range(N):
        if not visited[i]:
            left, right = very_left(i, visited), very_right(i, visited)
            if left == -1 or right == -1:
                pass
            else:
                visited[i] = True
                brute(visited, power + power_list[left] * power_list[right], count + 1)
                visited[i] = False

brute(visited, 0, 0)
print(max_power)
