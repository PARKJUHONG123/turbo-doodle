# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 21:13:16 2020

@author: elin9
"""

def pack(left_weight, item):    
    if item == N:
        return 0

    ret = cache[left_weight][item]
    if ret != -1:
        return ret
    ret = pack(left_weight, item + 1)
    
    if left_weight >= weight[item]:
        ret = max(ret, pack(left_weight - weight[item], item + 1) + need[item])
    cache[left_weight][item] = ret
    return ret

def reconstruct(left_weight, item):
    if item == N:
        return
    if pack(left_weight, item) == pack(left_weight, item + 1):
        reconstruct(left_weight, item + 1)
    else :
        picked.append(item)
        reconstruct(left_weight - weight[item], item + 1)

file = open("9_2_input.txt", "r")
C = int(file.readline())
for _ in range(C):
    N_W = list(map(int, file.readline().split()))
    N = N_W[0]
    W = N_W[1]
    
    name = ["" for _ in range(N)]
    weight = [0 for _ in range(N)]
    need = [0 for _ in range(N)]
    
    cache = [[-1 for _ in range(N)] for _ in range(W + 1)]

    for i in range(N):
        file_read = file.readline().split()
        name[i] = file_read[0]
        weight[i] = int(file_read[1])
        need[i] = int(file_read[2])

    ret = pack(W, 0)
    picked = []
    reconstruct(W, 0)
    print(ret, len(picked))
    for item in picked:
        print(name[item])