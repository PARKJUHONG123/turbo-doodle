# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:04:54 2020

@author: elin9
"""


n, m = input().split()
n = int(n) # meter
m = int(m) # days

cache = [[-1 for _ in range(n + m * 2)] for _ in range(m + 1)]

def climb(days, climbed):
    if days == m:
        if climbed >= n:
            return 1
        else :
            return 0
    
    ret = cache[days][climbed]
    if ret != -1:
        return ret
    ret = 3 * climb(days + 1, climbed + 1) + climb(days + 1, climbed + 2)
    cache[days][climbed] = ret
    return ret

print(climb(0, 0) / pow(4, m))