# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:36:53 2020

@author: elin9
"""

input_file = open("6_2_input.txt", "r")

C = int(input_file.readline())
count = 0

def brute_force(inner_set, visited, phase, n, m, all_set):
    if phase == m :
        if len(all_set) == len(visited) and all_set == set(visited):
            global count
            count += 1
            return True
        else :
            return False
        
    brute_force(inner_set, visited, phase + 1, n, m, all_set)
    brute_force(inner_set, visited + inner_set[phase], phase + 1, n, m, all_set)
        
        
for _ in range(C):
    n, m = input_file.readline().split()
    n = int(n) # students num
    m = int(m) # innerset num
    inner_set = []
    set_line = input_file.readline().split()
    
    j = 0
    while(j < 2 * m):
        inner_set.append([int(set_line[j]), int(set_line[j + 1])])
        j = j + 2

    visited = []
    phase = 0
    count = 0
    all_set = set([k for k in range(n)])
    
    brute_force(inner_set, visited, phase, n, m, all_set)
    print(count)

input_file.close()

