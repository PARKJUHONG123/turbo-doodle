import sys

n = int(sys.stdin.readline())
max_day = -1
days = [[] for _ in range(10001)]

for _ in range(n):
    p, d = map(int, sys.stdin.readline().split())
    max_day = max(d, max_day)
    days[d].append(p)

stack = list()
total = 0
for i in reversed(range(1, max_day + 1)):
    if days[i]:
        stack.extend(days[i])
    if stack:
        max_value = max(stack)
        total += max_value
        stack.remove(max_value)
print(total)
