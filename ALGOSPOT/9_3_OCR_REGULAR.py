# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:19:12 2020

@author: elin9
"""

def text_to_number(test, n):
    ret = []
    for i in range(n):
        for j in range(m):
            if test[i] == word[j]:
                ret.append(j)
    return ret

def reconstruct(segment, previous):
    choose = choice[segment][previous]
    ret = word[choose]
    if segment < n - 1:
        ret = ret + " " + reconstruct(segment + 1, choose)
    return ret

def recognize(segment, previous):
    if segment == n:
        return 0
    ret = cache[segment][previous]
    if ret != 1.0:
        return ret
    ret = -1e200
    for this in range(m):
        cand = T[previous][this] + M[this][R[segment]] + recognize(segment + 1, this)
        if ret < cand:
            cache[segment][previous] = ret = cand
            choice[segment][previous] = this
    return ret

file = open("9_3_input.txt", "r")
m_q = list(map(int, file.readline().split()))
m = m_q[0]
q = m_q[1]

word = file.readline().split()
B = list(map(float, file.readline().split()))
T = [[0.0 for _ in range(m)] for _ in range(m)]
M = [[0.0 for _ in range(m)] for _ in range(m)]

for i in range(m):
    T_input = file.readline().split()
    for j in range(m):
        T[i][j] = float(T_input[j])

for i in range(m):
    M_input = file.readline().split()
    for j in range(m):
        M[i][j] = float(M_input[j])

for _ in range(q):
    q_input = file.readline().split()
    n = int(q_input[0])
    test = q_input[1:]
    choice = [[-1 for _ in range(m)] for _ in range(n)]
    cache = [[1.0 for _ in range(m)] for _ in range(n)]
    R = text_to_number(test, n)
    
    recognize(0, 0)
    print(reconstruct(0, 0))

