# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:46:16 2020

@author: elin9
"""

file = open("9_2_input.txt", "r")
C = int(file.readline())

def package(index, weight_sum, need_sum):
    if index == N:
        return need_sum
    ret = cache[index]
    if ret != -1:
        return ret
    print(need_sum)
    add_version = 0
    not_add_version = 0
    
    if weight_sum + weight[index] <= W:
        add_version = package(index + 1, weight_sum + weight[index], need_sum + need[index])
        chosen.append(index)
    not_add_version = package(index + 1, weight_sum, need_sum)
    
    ret = max(add_version, not_add_version)
    cache[index] = ret
    return ret
    
for _ in range(C):
    N_W = list(map(int, file.readline().split()))
    N = N_W[0]
    W = N_W[1]
    name = ["" for _ in range(N)]
    weight = [0 for _ in range(N)]
    need = [0 for _ in range(N)]
    cache = [-1 for _ in range(N)]
    chosen = []
    for i in range(N):
        file_read = file.readline().split()
        name[i] = file_read[0]
        weight[i] = int(file_read[1])
        need[i] = int(file_read[2])

    print(package(0, 0, 0), len(chosen))
    for index in chosen:
        print(name[index])
    
    