# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:27:30 2020

@author: elin9
"""


MOD = 1000000007

file = open("8_12_input.txt", "r")
C = int(file.readline())

def tile(i):    
    ret = cache[i]
    if ret != -1:
        return ret
    ret = tile(i - 1) + tile(i - 2)
    cache[i] = ret % MOD
    return ret

def sym_tile(i):
    if i % 2 == 0:
        i = int(i / 2)
        return (cache[i - 1] + cache[i]) % MOD
    else:
        i = int(i / 2)
        return cache[i]

def calc(i):
    if i > 2:
        cache[0] = 0
        cache[1] = 1
        cache[2] = 2
        tile(i)
        return (cache[i] - sym_tile(i)) % MOD
    else:
        if i == 0:
            return 0
        elif i == 1:
            return 0
        elif i == 2:
            return 0

for _ in range(C):
    n = int(file.readline())
    cache = [-1 for _ in range(n + 1)]
    print(calc(n))
