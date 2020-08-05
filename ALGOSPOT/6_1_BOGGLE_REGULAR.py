# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 16:55:33 2020

@author: elin9
"""

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]
LENGTH = 5
ARROW_LENGTH = 8

def in_range(y, x):
    if y >= LENGTH or x >= LENGTH:
        return False
    return True

def has_word(y, x, word):
    if (not in_range(y, x)):
        return False
    if board[y][x] != word[0]:
        return False
    if len(word) == 1 :
        return True
    
    for direction in range(ARROW_LENGTH):
        next_y = y + dy[direction]
        next_x = x + dx[direction]
        
        if (has_word(next_y, next_x, word[1:])):
            return True

def test_function(box_length, test_word):
    for i in range(box_length):
        for j in range(box_length):
            if has_word(j, i, test_word):
                return True
    return False


file = open("6_1_input.txt", "r")    
C = int(file.readline())
for _ in range(C):
    board = [[] for _ in range(LENGTH)]
    for i in range(LENGTH):
        input_str = file.readline()
        for j in range(LENGTH):
            board[i].append(input_str[j])
    
    W = int(file.readline())
    for _ in range(W):
        test_word = file.readline()
        test_word = test_word[:-1]
        if test_function(LENGTH, test_word):
            print(test_word, "YES")
        else:
            print(test_word, "NO")