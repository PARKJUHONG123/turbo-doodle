# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:41:37 2020

@author: elin9
"""

##  ##  #    #
#    #  ##  ##
cover_type = [[[0, 0], [1, 0], [0, 1]],
              [[0, 0], [0, 1], [1, 1]],
              [[0, 0], [1, 0], [1, 1]],
              [[0, 0], [1, 0], [1, -1]]]

def set(board, y, x, typo, delta):
    covered = True
    for i in range(3):
        ny = y + cover_type[typo][i][0]
        nx = x + cover_type[typo][i][1]
        
        if (ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0])):
            return False, board
        
        board[ny][nx] += delta
        if (board[ny][nx]) > 1:
            covered = False
    return covered, board

def cover(board):
    y = -1
    x = -1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                y = i
                x = j
                break
        if y != -1:
            break
    
    if y == -1:
        return 1
    
    ret = 0
    for typo in range(4):
        return_value, board = set(board, y, x, typo, 1)
        if (return_value == True):
            ret += cover(board)
        return_value, board = set(board, y, x, typo, -1)
    return ret
        
file = open("6_3_input.txt", "r")
C = int(file.readline())

for _ in range(C):
    H_W = list(map(int, file.readline().split()))    
    board = [[1 for _ in range(H_W[1])] for _ in range(H_W[0])]

    for i in range(H_W[0]):
        board_input = file.readline()
        for j in range(H_W[1]):
            if board_input[j] == '#':
                board[i][j] = 1
            else:
                board[i][j] = 0

    print(cover(board))    