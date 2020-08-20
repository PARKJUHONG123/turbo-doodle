# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 18:46:37 2020

@author: elin9
"""

n = int(input())

MOD = 1000000007
cache = [-1 for _ in range(n + 1)]

def tile(width):
    if width <= 1:
        return 1
    ret = cache[width]
    if ret != -1:
        return ret

    ret = (tile(width - 2) + tile(width - 1)) % MOD
    cache[width] = ret
    return ret

print(tile(n))