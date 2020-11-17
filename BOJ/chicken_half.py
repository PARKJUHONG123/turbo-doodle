import sys

A, B, C, X, Y = map(int, sys.stdin.readline().split())

value = 0
if X > Y:
    if A + B > C * 2:
        value += C * 2 * Y
    else:
        value += (A + B) * Y
    value += min(A * (X - Y), C * 2 * (X - Y))
else:
    if A + B > C * 2:
        value += C * 2 * X
    else:
        value += (A + B) * X
    value += min(B * (Y - X), C * 2 * (Y - X))

print(value)