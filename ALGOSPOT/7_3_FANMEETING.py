# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:30:07 2020

@author: elin9
"""

def check(member, fan, member_num, fan_start):
    for i in range(member_num):
        if member[i] == 'M' and fan[fan_start + i] == 'M':
            return False
    return True

file = open("7_3_input.txt", "r")
C = int(file.readline())

for _ in range(C):
    member = []
    member_input = file.readline()
    member_num = len(member_input) - 1
    for i in range(member_num):
        member.append(member_input[i])
    
    fan = []
    fan_input = file.readline()
    fan_num = len(fan_input) - 1
    for i in range(fan_num):
        fan.append(fan_input[i])

    count = 0
    for i in range(fan_num - member_num + 1):
        if check(member, fan, member_num, i):
            count += 1

    print(member)
    print(fan)
    print(count)