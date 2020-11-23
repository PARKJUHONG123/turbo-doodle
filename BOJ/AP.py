import sys
N = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().split()))
INF = 10 ** 20
min_count = INF

if N == 1:
    print(0)
else:
    for i in range(-1, 2):
        a = num_list[0] + i
        for j in range(-1, 2):
            b = num_list[1] + j
            dist = b - a
            before_value = b
            flag = False
            count = abs(i) + abs(j)
            for index in range(2, N):
                inner_dist = num_list[index] - before_value
                if dist == inner_dist:
                    before_value = num_list[index]
                elif dist == inner_dist + 1:
                    before_value = num_list[index] + 1
                    count += 1
                elif dist == inner_dist - 1:
                    before_value = num_list[index] - 1
                    count += 1
                else:
                    flag = True
                    break
            if not flag:
                min_count = min(count, min_count)
    print(min_count if min_count != INF else -1)