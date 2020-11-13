import sys
N = int(sys.stdin.readline().strip())

num_list = list()
for i in range(N):
    V = int(sys.stdin.readline().strip())
    num_list.append([V, i])

num_list.sort()

max_count = -1
for i in range(N):
    max_count = max(max_count, num_list[i][1] - i)
    print(num_list[i], i)
print(max_count + 1)