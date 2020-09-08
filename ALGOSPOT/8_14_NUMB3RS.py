# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 15:04:08 2020

@author: elin9
"""

file = open("8_14_input.txt", "r")

C = int(file.readline())

def set_percentage(village):
    cache = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        count = 0
        for j in range(N):
            if village[i][j] == 1:
                count += 1
        for j in range(N):
            if village[i][j] == 1:
                cache[i][j] = count
    return cache


def find_doonibal(start_vil, next_vil, left_day):
    if left_day == 0:
        if start_vil == next_vil:
            return 1
        else :
            return 0
    ret = 0
    
    for i in range(N):
        if village[start_vil][i] == 1:
            ret += 1 / cache[start_vil][i] * find_doonibal(i, next_vil, left_day - 1)
    return ret

for _ in range(C):
    NDP = list(map(int, file.readline().split()))
    N, D, P = NDP[0], NDP[1], NDP[2] #VILLAGE NUMBER #ESCAPE DAYS #PRISON VILLAGE
    village = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        village_input = list(map(int, file.readline().split()))
        for j in range(N):
            village[i][j] = village_input[j]
            
    T = int(file.readline())
    Q = list(map(int, file.readline().split()))
    cache = set_percentage(village)
    for i in range(T):
        print(find_doonibal(P, Q[i], D), end = ' ')
    print("")

