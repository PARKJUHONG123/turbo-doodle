import sys

N, M = map(int, sys.stdin.readline().split())
play = list(map(int, sys.stdin.readline().split()))

left_child = N - M
if left_child > 0:
    left, right = 0, N * max(play)
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for i in range(M):
            count += mid // play[i]

        if count < left_child:
            left = mid + 1
        else:
            right = mid - 1

    done_child = 0
    before_finish_day, finish_day = left - 1, left
    for i in range(M):
        done_child += before_finish_day // play[i]

    end_child = left_child - done_child
    for i in range(M):
        if (finish_day // play[i]) * play[i] == finish_day:
            end_child -= 1
        if end_child == 0:
            print(i + 1)
            break
else:
    print(N)