# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 16:32:41 2020

@author: elin9
"""

# combination (pick m elements from n elements)

def pick(n, picked, m):
    if (m == 0):
        print(picked)
        return
        
    if len(picked) == 0 :
        smallest = 0
    else :
        smallest = picked[-1] + 1

    for next in range(smallest, n):
        picked.append(next)
        pick(n, picked, m - 1)
        picked.pop()


pick(5, [], 3)