# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:53:17 2020

@author: elin9
"""

switch = [[0, 1, 2],
          [3, 7, 9, 11],
          [4, 10, 14, 15],
          [0, 4, 5, 6, 7],
          [6, 7, 8, 10, 12],
          [0, 2, 14, 15],
          [3, 14, 15],
          [4, 5, 7, 14, 15],
          [1, 2, 3, 4, 5],
          [3, 4, 5, 9, 13]]
switch_num = 10
clock_num = 16
inf = 123456789
clockwise = 4

def all_aligned(current_clock):
    for i in range(clock_num):
        if current_clock[i] != 12:
            return False
    return True

def push(current_clock, switch_index):
    for index in switch[switch_index]:
        current_clock[index] += 3
        if current_clock[index] == 15:
            current_clock[index] = 3

def brute_force(current_clock, switch_index):
    if switch_index == switch_num:
        if all_aligned(current_clock) == True:
            return 0
        return inf

    ret = inf
    for push_count in range(clockwise):
        ret = min(ret, push_count + brute_force(current_clock, switch_index + 1))
        push(current_clock, switch_index)
    return ret

file = open("6_4_input.txt", "r")
C = int(file.readline())
for _ in range(C):
    file_read = file.readline().split()
    switch_count = [0 for _ in range(switch_num)]
    current_clock = [int(k) for k in file_read]
    print(brute_force(current_clock, 0))
    
    
