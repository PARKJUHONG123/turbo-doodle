# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:19:12 2020

@author: elin9
"""
def print_m(A):
    for i in range(len(A)):
        print(A[i])
    print("")

def OCR(sentence):
    return sentence

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


print_m(T)
print_m(M)

for _ in range(q):
    q_input = file.readline().split()
    n = int(q_input[0])
    test = q_input[1:]
    print(OCR(test))
    



