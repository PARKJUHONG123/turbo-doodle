# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:31:23 2020

@author: elin9
"""

pixel_index = 0
def reverse(compressed):
    global pixel_index

    head = compressed[pixel_index]
    pixel_index += 1

    if head == 'b' or head == 'w':
        return head
    
    nw = reverse(compressed)
    ne = reverse(compressed)
    sw = reverse(compressed)
    se = reverse(compressed)
    
    return 'x' + sw + se + nw + ne
    
file = open("7_1_input.txt", "r")
C = int(file.readline())

for _ in range(C):
    pixel_index = 0
    line = file.readline()[:-1]
    compressed = [' ' for _ in range(len(line))]
    
    for i in range(len(compressed)):
        compressed[i] = line[i]
    
    reversed_pixel = ""
    while(pixel_index < len(compressed)):
        reversed_pixel += reverse(compressed)
    print(reversed_pixel)
    print("")