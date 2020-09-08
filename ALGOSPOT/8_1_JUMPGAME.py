# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 12:42:53 2020

@author: elin9
"""

file = open("8_1_input.txt", "r")

n = int(file.readline())
board = [[0 for _ in range(n)] for _ in range(n)]
cache = [[-1 for _ in range(n)] for _ in range(n)]

def jump(y, x):
    if y >= n or x >= n:
        return 0
    if y == n - 1 and x == n - 1:
        return 1
    ret = cache[y][x]
    if ret != -1:
        return ret

    jump_size = board[y][x]
    ret = (jump(y + jump_size, x) or jump(y, x + jump_size))
    cache[y][x] = ret
    return ret

for i in range(n):
    board_input = file.readline()
    board_input = board_input.split()
    for j in range(n):
        board[i][j] = int(board_input[j])

if jump(0, 0) == 1:
    print("TRUE")
else :
    print("FALSE")
print(cache)