# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 19:13:51 2020

@author: elin9
"""

file = open("8_9_input.txt", "r")
N = int(file.readline())

cache = [[-1 for _ in range(i + 1)] for i in range(N)]
tri = [[-1 for _ in range(i + 1)] for i in range(N)]

def tri_path(i, j):
    if i < j:
        return 0
    if i >= N or j >= N:
        return 0
    
    ret = cache[i][j]
    if ret != -1:
        return ret

    ret = max(tri_path(i + 1, j + 1), tri_path(i + 1, j)) + tri[i][j]
    cache[i][j] = ret
    return ret

def find_path(i, j, optimal):
    if i < j:
        return 0
    if i >= N or j >= N:
        return 0

    if optimal == tri[i][j]:
        return 1
    
    ret = 0
    if optimal == cache[i + 1][j + 1] + tri[i][j]:
        ret += find_path(i + 1, j + 1, optimal - tri[i][j])
    if optimal == cache[i + 1][j] + tri[i][j] :
        ret += find_path(i + 1, j, optimal - tri[i][j])
    return ret

for i in range(N): 
    file_input = list(map(int, file.readline().split()))
    for j in range(i + 1):
        tri[i][j] = file_input[j]

optimal = tri_path(0, 0)
print(find_path(0, 0, optimal))
