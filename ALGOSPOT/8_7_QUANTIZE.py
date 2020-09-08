# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:57:49 2020

@author: elin9
"""

INF = 987654321
file = open("8_7_input.txt", "r")
C = int(file.readline())

def pre_calc():
    T.sort()
    pre_sum[0] = T[0]
    pre_seq_sum[0] = T[0] * T[0]
    
    for i in range(n):
        pre_sum[i] = pre_sum[i - 1] + T[i]
        pre_seq_sum[i] = pre_seq_sum[i - 1] + T[i] * T[i]

def min_error(lo, hi):
    if lo == 0:
        _sum = pre_sum[hi]
        seq_sum = pre_seq_sum[hi]
    else :
        _sum = pre_sum[hi] - pre_sum[lo - 1]
        seq_sum = pre_seq_sum[hi] - pre_seq_sum[lo - 1]
    
    m = int(0.5 + _sum / (hi - lo + 1))
    ret = seq_sum - (2 * m * _sum) + (m * m * (hi - lo + 1))
    return ret

def quantize(start, parts):
    if start == n :
        return 0
    if parts == 0:
        return INF
    ret = cache[start][parts]
    if ret != -1:
        return ret
    
    ret = INF
    for part_size in range(1, n + 1 - start):
        ret = min(ret, min_error(start, start + part_size - 1) + quantize(start + part_size, parts - 1))
    cache[start][parts] = ret
    return ret
    
for _ in range(C):
    n_s = list(map(int, file.readline().split()))
    n = n_s[0] 
    s = n_s[1]
    
    T = list(map(int, file.readline().split()))
    cache = [[-1 for _ in range(s + 1)] for _ in range(n + 1)]
    pre_sum = [0 for _ in range(n + 1)]
    pre_seq_sum = [0 for _ in range(n + 1)]
    
    pre_calc()
    print(quantize(0, s))   