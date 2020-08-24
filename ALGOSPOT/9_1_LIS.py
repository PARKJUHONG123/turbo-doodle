# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 17:27:10 2020

@author: elin9
"""

def lis4(start):
    ret = cache[start + 1]
    if ret != -1:
        return ret
    ret = 1
    best_next = -1
    for next in range(start + 1, n):
        if start == -1 or S[start] < S[next]:
            cand = lis4(next) + 1
            if cand > ret:
                ret = cand
                best_next = next
    choices[start + 1] = best_next
    cache[start + 1] = ret
    return ret

def reconstruct(start):
    if start != -1:
        seq.append(S[start])
    next = choices[start + 1]
    if next != -1:
        reconstruct(next)

S = [3, 8, 14, 2, 4, 15, 9, 12, 13]
n = len(S)
cache = [-1 for _ in range(n + 1)]
choices = [-1 for _ in range(n + 1)]
seq = []

ret = lis4(-1)
reconstruct(-1)
print(ret)
print(seq)