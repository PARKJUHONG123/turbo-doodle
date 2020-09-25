import sys

T = int(sys.stdin.readline())
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

A_dict, B_dict = dict(), dict()
for i in range(N):
    inner_total = 0
    for j in range(i, N):
        inner_total += N_list[j]
        if inner_total in A_dict:
            A_dict[inner_total] += 1
        else:
            A_dict[inner_total] = 1

for i in range(M):
    inner_total = 0
    for j in range(i, M):
        inner_total += M_list[j]
        if inner_total in B_dict:
            B_dict[inner_total] += 1
        else:
            B_dict[inner_total] = 1

count = 0
for i in A_dict.keys():
    if T - i in B_dict:
        count += (A_dict[i] * B_dict[T - i])
print(count)