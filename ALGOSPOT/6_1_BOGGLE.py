# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 21:56:24 2020

@author: elin9
"""
#import sys
LENGTH = 5
ARROW = 9
x_arrow = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
y_arrow = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

# C = int(sys.stdin.readline())
C = int(input())

for _ in range(C):
    str_input = [[] for _ in range(LENGTH)]
    for i in range(LENGTH):        
        #str_input[i] = sys.stdin.readline()
        str_input[i] = input()
    
    W = int(input())
    test_word = ""
    
    def hasWord(y, x, word):
        if word == len(test_word) - 1 and test_word[word] == str_input[y][x]:
            return True
        
        if test_word[word] != str_input[y][x]:
            return False
    
        for i in range(ARROW):
            if 0 <= y + y_arrow[i] < LENGTH and 0 <= x + x_arrow[i] < LENGTH:
                if hasWord(y + y_arrow[i], x + x_arrow[i], word + 1):
                    return True
        return False
    
    for _ in range(W):
        early_break = False
        test_word = input()
        for i in range(LENGTH):
            for j in range(LENGTH):
                if hasWord(i, j, 0) == True:
                    early_break = True
                    break
            if early_break == True:
                break
        print(test_word, early_break)

#import os
#os.system("pause")    