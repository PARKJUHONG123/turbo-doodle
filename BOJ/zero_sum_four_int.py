import sys

n = int(sys.stdin.readline())
A, B, C, D = [0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(n)]
for i in range(n):
    A[i], B[i], C[i], D[i] = map(int, sys.stdin.readline().split())

A, B, C, D = sorted(A), sorted(B), sorted(C), sorted(D)

x = dict()
for a in A:
    for b in B:
        if a + b in x:
            x[a + b] += 1
        else:
            x[a + b] = 1

y = dict()
for c in C:
    for d in D:
        if c + d in y:
            y[c + d] += 1
        else:
            y[c + d] = 1

count = 0
for value in x.keys():
    if -value in y:
        count += x[value] * y[-value]

print(count)