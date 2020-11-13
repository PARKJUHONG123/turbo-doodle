import sys

N = int(sys.stdin.readline().strip())

num_dict = dict()
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if x in num_dict:
        num_dict[x].append(y)
    else:
        num_dict[x] = [y]

key_list = list(num_dict.keys())
key_list.sort()

for key in key_list:
    num_dict[key].sort()
    for value in num_dict[key]:
        print(key, value)
