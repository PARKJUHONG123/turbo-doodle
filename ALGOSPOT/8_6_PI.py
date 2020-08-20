# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:04:16 2020

@author: elin9
"""


file = open("8_6_input.txt", "r")
C = int(file.readline())

def range_3(T):
    score = [False for _ in range(6)]
    
    if T[0] == T[1] and T[1] == T[2]:
        score[1] = True
    
    elif abs(T[0] - T[1]) == 1 and T[0] - T[1] == T[1] - T[2]:
        score[2] = True
    
    elif T[0] == T[2]:
        score[4] = True
    
    elif T[0] - T[1] == T[1] - T[2]:
        score[5] = True

    if not True in score:
        return 10
    else:
        for i in range(6):
            if score[i] == True:
                return i
    
def range_4(T):
    score = [False for _ in range(6)]
    
    if T[0] == T[1] == T[2] == T[3]:
        score[1] = True
    
    elif abs(T[0] - T[1]) == 1 and T[0] - T[1] == T[1] - T[2] == T[2] - T[3]:
        score[2] = True
    
    elif T[0] == T[2] and T[1] == T[3]:
        score[4] = True
    
    elif T[0] - T[1] == T[1] - T[2] == T[2] - T[3]:
        score[5] = True

    if not True in score:
        return 10
    else:
        for i in range(6):
            if score[i] == True:
                return i
    
def range_5(T):
    score = [False for _ in range(6)]
    
    if T[0] == T[1] == T[2] == T[3] == T[4]:
        score[1] = True
    
    elif abs(T[0] - T[1]) == 1 and T[0] - T[1] == T[1] - T[2] == T[2] - T[3] == T[3] - T[4]:
        score[2] = True
    
    elif T[0] == T[2] == T[4] and T[1] == T[3]:
        score[4] = True
    
    elif T[0] - T[1] == T[1] - T[2] == T[2] - T[3] == T[3] - T[4]:
        score[5] = True

    if not True in score:
        return 10
    else:
        for i in range(6):
            if score[i] == True:
                return i
        
for _ in range(C):
    T = []
    T_input = file.readline().split()[0]
    for i in range(len(T_input)):
        T.append(int(T_input[i]))
    
    ret = [0 for _ in range(len(T_input) + 1)] 
    ret[3] = range_3(T[:3])
    ret[4] = range_4(T[:4])
    ret[5] = range_5(T[:5])
    
    for i in range(6, len(T_input) + 1):
        v1 = range_3(T[i - 3 : i]) + ret[i - 3]
        v2 = range_4(T[i - 4 : i]) + ret[i - 4]
        v3 = range_5(T[i - 5 : i]) + ret[i - 5]
        ret[i] = min(min(v1, v2), v3)
    
    print(ret[-1])
        
        
        
        
        
        