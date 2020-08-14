# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:30:07 2020

@author: elin9
"""


file = open("7_3_input.txt", "r")

C = int(file.readline())

for _ in range(C):
    member = []
    member_input = file.readline()
    for i in range(len(member_input)):
        member.append(member_input[i])
    
    fan = []
    fan_input = file.readline()
    for i in range(len(fan_input)):
        fan.append(fan_input[i])
    
    print(member)
    print(fan)