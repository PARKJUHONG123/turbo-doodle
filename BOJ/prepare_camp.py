import sys

N, L, R, X = map(int, sys.stdin.readline().split())
problems = list(map(int, sys.stdin.readline().split()))
problems.sort()

def brute(index, total, min_value, max_value):
    ret = 0
    if index == N:
        if L <= total <= R and max_value - min_value >= X:
            return 1
        return 0
    ret += brute(index + 1, total, min_value, max_value)
    value = problems[index]
    ret += brute(index + 1, total + value, min(min_value, value), max(max_value, value))
    return ret

print(brute(0, 0, 987654321, -987654321))