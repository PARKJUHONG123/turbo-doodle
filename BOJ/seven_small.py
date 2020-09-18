import sys

n = 9
lst = [0 for _ in range(n)]
for i in range(n):
    lst[i] = int(sys.stdin.readline())

total = sum(lst)

token = False
for i in range(n):
    for j in range(i + 1, n):
        if total - (lst[i] + lst[j]) == 100:
            set_lst = set(lst)
            set_lst.remove(lst[i])
            set_lst.remove(lst[j])
            token = True
            break
    if token:
        break

ret = sorted(list(set_lst))
for value in ret:
    print(value)
