# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:41:07 2020

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

inf = 123456789
switch_num = len(switch)

def add_time(clock):
    clock += 3
    if clock == 15:
        return 3
    return clock

def push_switch(clock, switch_index):
    for connected_clock_index in switch[switch_index]:
        clock[connected_clock_index] = add_time(clock[connected_clock_index])
    return clock

def all_set(clock):
    for each_clock in clock:
        if each_clock != 12:
            return False
    return True

def brute_force(clock, switch_index):
    if all_set(clock):
        return 0
    
    if switch_index == len(switch):
        return inf
    
    ret = inf
    for count in range(4):
        ret = min(ret, count + brute_force(clock, switch_index + 1))
        push_switch(clock, switch_index)
    return ret

file = open("6_4_input.txt", "r")
C = int(file.readline())

for _ in range(C):
    clock = file.readline().split()
    clock = list(map(int, clock))
    ret = brute_force(clock, 0)    
    if ret >= inf:
        print(-1)
    else:
        print(ret)    