import sys

while True:
    try:
        N, M = map(int, sys.stdin.readline().split())
    except:
        exit()
    matrix = ['' for _ in range(N)]
    for i in range(N):
        matrix[i] = sys.stdin.readline().strip()

    
