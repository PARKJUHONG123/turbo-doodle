import sys
T = int(sys.stdin.readline())

for _ in range(T):
    M, N, x, y = list(map(int, sys.stdin.readline().split()))
    N_list = [False] * (N + 1)

    token = False
    while False in N_list:
        value = x % N
        if value == 0:
            value = N

        if value == y:
            token = True
            print(x)
            break
        else:
            if N_list[value]:
                break
            N_list[value] = True
            x = x + M
    if not token:
        print(-1)