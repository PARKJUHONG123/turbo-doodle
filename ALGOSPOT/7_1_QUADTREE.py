# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:31:23 2020

@author: elin9
"""


file = open("7_1_input.txt", "r")
C = int(file.readline())
    
def close_door(compressed, index):
    flag = -4
    i = index
    while True:
        if i >= len(compressed):
            return compressed
        if compressed[i] == 'x':
            flag -= 3
        elif compressed[i] == 'b' or compressed[i] == 'w':
            flag += 1
        i = i + 1
        if flag == 0:
            compressed.insert(i, ']')
            return compressed
        
for _ in range(C):
    line = file.readline()[:-1]
    compressed = [' ' for _ in range(len(line))]
    
    for i in range(len(compressed)):
        compressed[i] = line[i]
    i = 0
    while True:
        if i >= len(compressed):
            break
        
        if compressed[i] == 'x':
            compressed[i] = '['
            compressed = close_door(compressed, i)
        i = i + 1
            
    print(compressed)