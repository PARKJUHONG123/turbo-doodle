import sys
from math import sqrt
A = [0, 0, 0]
B = [0, 0, 0]
C = [0, 0, 0]
A[0], A[1], A[2], B[0], B[1], B[2], C[0], C[1], C[2] = map(float, sys.stdin.readline().split())

def mid_A_B(A, B):
    D = [0, 0, 0]
    for i in range(3):
        D[i] = (A[i] + B[i]) / 2
    return D

def calc_dist(X, Y):
    ret = 0
    for i in range(3):
        ret += (X[i] - Y[i]) ** 2
    return ret

bc_dist = calc_dist(B, C)
ac_dist = calc_dist(A, C)
count = 0
while count < 25:
    count += 1
    D = mid_A_B(A, B)
    bc_dist = calc_dist(B, C)
    ac_dist = calc_dist(A, C)
    if bc_dist < ac_dist:
        A = D
    else:
        B = D

print(format(sqrt(ac_dist), ".10f"))