# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:53:19 2020

@author: elin9
"""

file = open("8_2_input.txt", "r")
C = int(file.readline())


def match_memorized(w, s):
    ret = cache[w][s]
    if ret != -1:
        return ret
    
    if s < len(S) and w < len(W) and (W[w] == '?' or W[w] == S[s]):
        ret = match_memorized(w + 1, s + 1)
        cache[w][s] = ret
        return ret
    
    if w == len(W):
        if s == len(S):
            ret = 1
        else:
            ret = 0
        cache[w][s] = ret
        return ret
    
    if W[w] == '*':
        if match_memorized(w + 1, s) or (s < len(S) and match_memorized(w, s + 1)):
            ret = 1
            cache[w][s] = ret
            return ret

    ret = 0
    cache[w][s] = ret
    return ret
    
    
for _ in range(C):
    W = file.readline()[:-1]
    n = int(file.readline())
    for _ in range(n):
        cache = [[-1 for _ in range(101)] for _ in range(101)]
        S = file.readline()[:-1]
        if match_memorized(0, 0):
            print(S)
    
    
    