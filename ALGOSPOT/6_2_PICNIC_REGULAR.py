# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:04:58 2020

@author: elin9
"""

def permutation_count_pairs(taken):
    finished = True
    for i in range(n):
        if not (taken[i]):
            finished = False
    
    if (finished):
        return 1
    
    ret = 0
    for i in range(n):
        for j in range(n):
            if (not taken[i] and not taken[j] and matched[i][j]):
                taken[i] = taken[j]= True
                ret += permutation_count_pairs(taken)
                taken[i] = taken[j] = False
    return ret


def combination_count_pairs(taken):
    first_free = -1
    for i in range(n):
        if not (taken[i]):
            first_free = i
            break
    
    if (first_free == -1):
        return 1
    
    ret = 0
    for i in range(first_free + 1, n):
        if (not taken[first_free] and not taken[i] and matched[first_free][i]):
                taken[first_free] = taken[i] = True
                ret += combination_count_pairs(taken)
                taken[first_free] = taken[i] = False
    return ret


def match_friends(friends):
    matched = [[False for _ in range(n)] for _ in range(n)]
    for k in range(m):
        left = 2*k
        right = 2*k + 1
        matched[friends[left]][friends[right]] = True
        matched[friends[right]][friends[left]] = True
    return matched

file = open("6_2_input.txt", "r")
C = int(file.readline())

for _ in range(C):
    n_m = file.readline().split()
    n_m = list(map(int, n_m))
    n = n_m[0]
    m = n_m[1]

    taken = [False for _ in range(n)] 
    friends = file.readline().split()
    friends = list(map(int, friends))
    
    matched = match_friends(friends)        
    print(combination_count_pairs(taken))