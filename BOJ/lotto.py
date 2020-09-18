from itertools import combinations
import sys

lst = []
while True:
    tmp = sys.stdin.readline()
    if tmp[0] == '0':
        break
    tmp = tmp.split()
    tmp = tmp[1:]
    lst.append(list(map(int, tmp)))

for i in range(len(lst)):
    for value in list(combinations(lst[i], 6)):
        ret = list(value)
        ret.sort()

        ret_str = ""
        for element in ret:
            ret_str += str(element) + " "
        print(ret_str[:-1])
    if i != len(lst) - 1:
        print("")