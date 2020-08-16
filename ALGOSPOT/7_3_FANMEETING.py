# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:30:07 2020

@author: elin9
"""

def brute_check(member, fan, member_num, fan_start):
    for i in range(member_num):
        if member[i] == 'M' and fan[fan_start + i] == 'M':
            return False
    return True

def add_to(a, b, k): # a > b
    for i in range(k):
        b.insert(0, 0)

    index = 0    
    if len(a) > len(b):
        for index in range(len(b)):
            a[index] += b[index]
    else:
        for index in range(len(a)):
            a[index] += b[index]
        for j in range(index, len(b)):
            a.append(b[j])
    return a

def sub_from(a, b):
    for i in range(len(b)):
        a[i] = a[i] - b[i]
    return a

def normalize(num_array):
    num_array.append(0)
    for i in range(len(num_array) - 1):
        if num_array[i] < 0:
            borrow = int((abs(num_array[i]) + 9) / 10)
            num_array[i + 1] -= borrow
            num_array[i] += borrow * 10
        else:
            num_array[i + 1] += int(num_array[i] / 10)
            num_array[i] %= 10
        
    while (len(num_array) > 1 and num_array[-1] == 0):
        num_array.pop()
    return num_array

def multiply(a, b):
    a_len = len(a)
    b_len = len(b)
    c = [0 for _ in range(a_len + b_len + 1)]

    for i in range(a_len):
        for j in range(b_len):
            c[i + j] += a[i] * b[j]
    return c

def karatsuba(a, b):
    a_len = len(a)
    b_len = len(b)
    
    if a_len < b_len:
        return karatsuba(b, a)
    if a_len == 0 or b_len == 0:
        return []
    if a_len < 1:
        return multiply(a, b)
    
    half = int(a_len / 2)
    
    a_0 = a[0 : half]
    a_1 = a[half : - 1]
    b_0 = b[0 : min(b_len, half)]
    b_1 = b[min(b_len, half) : -1]

    z_2 = karatsuba(a_1, b_1)
    z_0 = karatsuba(a_0, b_0)

    a_0 = add_to(a_0, a_1, 0)
    b_0 = add_to(b_0, b_1, 0)

    z_1 = karatsuba(a_0, b_0)
    z_1 = sub_from(z_1, z_0)
    z_1 = sub_from(z_1, z_2)

    ret = []
    ret = add_to(ret, z_0, 0)
    ret = add_to(ret, z_1, half)
    ret = add_to(ret, z_2, half + half)
    return ret

def hug(member, fan):
    member_len = len(member)    
    fan_len = len(fan)
    
    member_math = [0 for _ in range(member_len)]
    fan_math = [0 for _ in range(fan_len)]
    
    for i in range(member_len):
        if member[i] == 'M':
            member_math[i] = 1
        else :
            member_math[i] = 0

    for i in range(fan_len):
        if fan[fan_len - i - 1] == 'M':
            fan_math[i] = 1
        else :
            fan_math[i] = 0

    calculated = karatsuba(member_math, fan_math)
    hug_count = 0

    for i in range(member_len - 1, fan_len):
        if calculated[i] == 0:
            hug_count += 1
    return hug_count

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
        if brute_check(member, fan, member_num, i):
            count += 1

    print(count)
    
    print(hug(member, fan))