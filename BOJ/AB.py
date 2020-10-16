import sys
N, M = map(int, sys.stdin.readline().split())

# B를 만났을 때 앞서서 본 A의 갯수
for i in range(N):
    a_num, b_num = i, N - i
    total = a_num * b_num
    target = M
    if total >= target:
        while True:
            if target >= b_num:
                target -= b_num
                if a_num > 0:
                    print('A', end = '')
                    a_num -= 1
            else:
                for j in range(b_num - target):
                    print('B', end = '')
                if a_num > 0:
                    print('A', end = '')
                    a_num -= 1
                for j in range(target):
                    print('B', end = '')
                exit()
print(-1)