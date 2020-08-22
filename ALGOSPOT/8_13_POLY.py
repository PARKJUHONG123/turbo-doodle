# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 19:10:21 2020

@author: elin9
"""

MOD = 10000000
file = open("8_13_input.txt", "r")
C = int(file.readline())


def poly(first_box, left_box):
    if left_box == first_box:
        return 1
    ret = cache[first_box][left_box]
    if ret != -1:
        return ret
    
    ret = 0
    next_able = left_box - first_box
    for second_box in range(1, next_able + 1):
        add = (first_box + second_box - 1) * poly(second_box, left_box - first_box)
        add %= MOD
        ret += add
        ret %= MOD        
    cache[first_box][left_box] = ret
    return ret

def calc_poly(n):
    ret = 0
    for i in range(1, n + 1):
        ret += poly(i, n)
        ret %= MOD
    return ret
        
for _ in range(C):
    n = int(file.readline())
    cache = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    print(calc_poly(n))
        