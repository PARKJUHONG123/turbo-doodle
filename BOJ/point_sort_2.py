import sys

N = int(sys.stdin.readline().strip())

num_dict = dict()
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if y in num_dict:
        num_dict[y].append(x)
    else:
        num_dict[y] = [x]

key_list = list(num_dict.keys())
key_list.sort()

for key in key_list:
    num_dict[key].sort()
    for value in num_dict[key]:
        print(value, key)
