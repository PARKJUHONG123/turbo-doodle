import sys
R, C = map(int, sys.stdin.readline().split())

dir_x, dir_y = [-1, 0, 0, 1], [0, -1, 1, 0]
ret = ""
if R % 2 == 1:
    for i in range(C):
        if i % 2 == 0:
            ret += 'D' * (R - 1) + 'R'
        else:
            ret += 'U' * (R - 1) + 'R'
    print(ret[:-1])

else:
    if C % 2 == 1:
        for i in range(C):
            if i % 2 == 0:
                ret += 'D' * (R - 1) + 'R'
            else:
                ret += 'U' * (R - 1) + 'R'
        print(ret[:-1])
    else:
        min_index, min_num = [0, 0], 1001
        for i in range(R):
            tmp = list(map(int, sys.stdin.readline().split()))
            for j in range(C):
                if (i + j) % 2 == 1:
                    if min_num > tmp[j]:
                        min_num = tmp[j]
                        min_index = [i, j]

        half_y = min_index[1] // 2
        R_ = R - 1
        ret = ('D' * R_ + 'R' + 'U' * R_ + 'R') * half_y
        x, y = 2 * half_y, 0
        x_bound = x + 1
        while x != x_bound or y != R_:
            if x < x_bound and [y, x_bound] != min_index:
                x += 1
                ret += 'R'
            elif x == x_bound and [y, x_bound - 1] != min_index:
                x -= 1
                ret += 'L'
            if y != R_:
                y += 1
                ret += 'D'

        ret += ('R' + 'U' * R_ + 'R' + 'D' * R_) * ((C - min_index[1] - 1) // 2)
        print(ret)
