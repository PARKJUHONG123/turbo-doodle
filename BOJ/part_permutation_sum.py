import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
length = len(num_list)
visited = set()

def brute(index, total):
    if index < length:
        brute(index + 1, total + num_list[index])
        brute(index + 1, total)
    elif index == length:
        visited.add(total)
brute(0, 0)

max_value = max(visited) + 2
for i in range(max_value):
    if i not in visited:
        print(i)
        break
