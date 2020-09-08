# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 18:55:58 2020

@author: elin9
"""

def search(y, x):
    if y + 1 > n or x + 1 > n:
        return 0

    ret = cache[y][x]
    if ret != -1:
        return ret    

    ret = max(search(y + 1, x), search(y + 1, x + 1)) + tri[y][x]
    cache[y][x] = ret
    return ret

file = open("8_3_input.txt", "r")
n = int(file.readline())

tri = [[0 for _ in range(i + 1)] for i in range(n)]
cache = [[-1 for _ in range(i + 1)] for i in range(n)]

for i in range(n):
    tri[i] = list(map(int, file.readline().split()))

print(search(0, 0))
print(tri)
print(cache)