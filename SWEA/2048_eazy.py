import sys
N = int(sys.stdin.readline())
arr = [[0 for _ in range(N)] for _ in range(N)]
max_num = -1

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    max_num = max(max_num, max(tmp))
    for j in range(N):
        arr[i][j] = tmp[j]

def brute_force(arr, max_num, count, dir):
    ret = max_num
    if count > 4:
        return ret
    drr = []
    if dir == 0:
        for i in range(N):
            zero_count = 0
            tmp = []
            mixed = False

            for j in range(N):
                if arr[i][j] == 0:
                    zero_count += 1
                else:
                    if tmp:
                        if arr[i][j] == tmp[-1] and not mixed:
                            tmp[-1] *= 2
                            max_num = max(max_num, tmp[-1])
                            zero_count += 1
                            mixed = True
                        else:
                            mixed = False
                            tmp.append(arr[i][j])
                    else:
                        tmp.append(arr[i][j])
            tmp.extend([0 for _ in range(zero_count)])
            drr.append(tmp)

    elif dir == 1:
        for i in range(N):
            zero_count = 0
            tmp = []
            mixed = False

            for j in reversed(range(N)):
                if arr[i][j] == 0:
                    zero_count += 1
                else:
                    if tmp:
                        if arr[i][j] == tmp[0] and not mixed:
                            tmp[0] *= 2
                            max_num = max(max_num, tmp[0])
                            zero_count += 1
                            mixed = True
                        else:
                            mixed = False
                            tmp2 = [arr[i][j]]
                            tmp2.extend(tmp)
                            tmp = tmp2
                    else:
                        tmp = [arr[i][j]]
            if zero_count != 0:
                tmp2 = [0 for _ in range(zero_count)]
                tmp2.extend(tmp)
                tmp = tmp2
            drr.append(tmp)

    elif dir == 2:
        for j in range(N):
            zero_count = 0
            tmp = []
            mixed = False

            for i in range(N):
                if arr[i][j] == 0:
                    zero_count += 1
                else:
                    if tmp:
                        if arr[i][j] == tmp[-1] and not mixed:
                            tmp[-1] *= 2
                            max_num = max(max_num, tmp[-1])
                            zero_count += 1
                            mixed = True
                        else:
                            mixed = False
                            tmp.append(arr[i][j])
                    else:
                        tmp.append(arr[i][j])
            tmp.extend([0 for _ in range(zero_count)])
            drr.append(tmp)

        for i in range(N):
            for j in range(i + 1, N):
                num = drr[i][j]
                drr[i][j] = drr[j][i]
                drr[j][i] = num

    elif dir == 3:
        for j in range(N):
            zero_count = 0
            tmp = []
            mixed = False

            for i in reversed(range(N)):
                if arr[i][j] == 0:
                    zero_count += 1
                else:
                    if tmp:
                        if arr[i][j] == tmp[0] and not mixed:
                            tmp[0] *= 2
                            max_num = max(max_num, tmp[0])
                            zero_count += 1
                            mixed = True
                        else:
                            mixed = False
                            tmp2 = [arr[i][j]]
                            tmp2.extend(tmp)
                            tmp = tmp2
                    else:
                        tmp = [arr[i][j]]
            if zero_count != 0:
                tmp2 = [0 for _ in range(zero_count)]
                tmp2.extend(tmp)
                tmp = tmp2
            drr.append(tmp)

        for i in range(N):
            for j in range(i + 1, N):
                num = drr[i][j]
                drr[i][j] = drr[j][i]
                drr[j][i] = num

    for i in range(4):
        ret = max(ret, brute_force(drr, max_num, count + 1, i))
    return ret

for i in range(4):
    max_num = max(max_num, brute_force(arr, max_num, 0, i))
print(max_num)