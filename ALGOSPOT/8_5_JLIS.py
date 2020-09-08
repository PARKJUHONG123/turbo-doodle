# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:51:52 2020

@author: elin9
"""

file = open("8_5_input.txt", "r")
C = int(file.readline())
NEGINF = float('-inf')

def jlis_regular(a_index, b_index):
    ret = cache[a_index + 1][b_index + 1]
    if ret != -1:
        return ret

    ret = 2
    if a_index == -1:
        a = NEGINF
    else:
        a = A[a_index]

    if b_index == -1:
        b = NEGINF
    else:
        b = B[b_index]
    max_element = max(a, b)
    
    for next_a in range(a_index + 1, n):
        if max_element < A[next_a]:
            ret = max(ret, jlis_regular(next_a, b_index) + 1)
    for next_b in range(b_index + 1, m):
        if max_element < B[next_b]:
            ret = max(ret, jlis_regular(a_index, next_b) + 1)

    cache[a_index + 1][b_index + 1] = ret
    return ret
       
for _ in range(C):
    n_m = list(map(int, file.readline().split()))
    n = n_m[0]
    m = n_m[1]
    A = list(map(int, file.readline().split()))
    B = list(map(int, file.readline().split()))
    
    cache = [[-1 for _ in range(101)] for _ in range(101)]
    print(jlis_regular(-1, -1) - 2)
