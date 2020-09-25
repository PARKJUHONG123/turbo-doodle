import copy
import sys

def brute_force(visited, phase, n):
    ret = 0
    to_visit = [0 for _ in range(n)]
    if phase != 0:
        for i in range(n):
            value = visited[i]
            if value == 1:
                if i != 0:
                    to_visit[i - 1] += 1
            elif value == 2:
                if i != n - 1:
                    to_visit[i + 1] += 2
            elif value == 3:
                if i != 0:
                    to_visit[i - 1] += 1
                if i != n - 1:
                    to_visit[i + 1] += 2
            elif value == 4:
                to_visit[i] += 4
            elif value == 5:
                to_visit[i] += 4
                if i != 0:
                    to_visit[i - 1] += 1
            elif value == 6:
                to_visit[i] += 4
                if i != n - 1:
                    to_visit[i + 1] += 2
            elif value >= 7:
                to_visit[i] += 4
                if i != 0:
                    to_visit[i - 1] += 1
                if i != n - 1:
                    to_visit[i + 1] += 2

    if phase == n - 1:
        for i in range(n):
            if to_visit[i] == 0:
                ret += 1
        return ret

    for i in range(n):
        if to_visit[i] == 0:
            to_visit[i] = 7
            ret += brute_force(to_visit, phase + 1, n)
            to_visit[i] = 0
    return ret

n = int(sys.stdin.readline().split()[0])
visited = [0 for _ in range(n)]
print(brute_force(visited, 0, n))