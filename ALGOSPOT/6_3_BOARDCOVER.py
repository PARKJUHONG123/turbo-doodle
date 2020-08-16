# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 22:50:01 2020

@author: elin9
"""

import copy

file = open("6_3_input.txt", "r")
C = int(file.readline())

# *   | * * |   * | * * | 
# * * | *   | * * |   * |

count = 0

def inner_function(board, i, j, i1, j1, i2, j2, i3, j3):
    board[i1][j1] = '#'
    board[i2][j2] = '#'
    board[i3][j3] = '#'
    brute_force(board, i, j + 1)
    board[i1][j1] = '.'
    board[i2][j2] = '.'
    board[i3][j3] = '.'
    
def brute_force(board, i, j):
    if j == W - 1:
        i = i + 1
        j = 0
    
    if i == H - 1 and j == 0:
        for a in range(H):
            for b in range(W):
                if '.' == board[a][b]:
                    return False
        
        global count
        count += 1
        return True        
        
    if board[i][j] == '.' and board[i][j + 1] == '.' and board[i + 1][j] == '.':
        inner_function(board, i, j, i, j, i, j + 1, i + 1, j)
        
    if board[i][j] == '.' and board[i][j + 1] == '.' and board[i + 1][j + 1] == '.':
        inner_function(board, i, j, i, j, i, j + 1, i + 1, j + 1)
    
    if board[i][j] == '.' and board[i + 1][j] == '.' and board[i + 1][j + 1] == '.':
        inner_function(board, i, j, i, j, i + 1, j, i + 1, j + 1)

    if board[i][j + 1] == '.' and board[i + 1][j] == '.' and board[i + 1][j + 1] == '.':
        inner_function(board, i, j, i, j + 1, i + 1, j, i + 1, j + 1)

    if board[i][j] == '#':
        brute_force(board, i, j + 1)

for _ in range(C):
    H, W = file.readline().split()
    H = int(H)
    W = int(W)
    board = [[] for _ in range(H)]
    
    for i in range(H):
        line = file.readline()
        for j in range(W):
            board[i].append(line[j])
    brute_force(board, 0, 0)
    print(count)
    count = 0