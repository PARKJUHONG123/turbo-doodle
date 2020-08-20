# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 18:46:37 2020

@author: elin9
"""

n = int(input())

cache = [0 for _ in range(n)]
cache[0] = 1
cache[1] = 2
for i in range(2, n):
    cache[i] = cache[i - 1] + cache[i - 2]

print(cache[-1])