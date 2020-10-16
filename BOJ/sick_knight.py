import sys
N, M = map(int, sys.stdin.readline().split())

count = 1
if N > 2 and M > 6:
    M -= 7
    count += (4 + M)

else:
    if N > 2: # == M <= 6
        if M >= 4:
            count = 4
        else:
            count = M
    elif N == 2:
        left = (M - 1) // 2
        count += (3 if left >= 3 else left)

print(count)
