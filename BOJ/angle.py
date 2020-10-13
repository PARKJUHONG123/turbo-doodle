import sys
N, K = map(int, sys.stdin.readline().split())

ready_angle = list(map(int, sys.stdin.readline().split()))
need_angle = list(map(int, sys.stdin.readline().split()))

can_make = [False for _ in range(361)]
can_make[0], can_make[360] = True, True

for value in ready_angle:
    for i in range(360):
        if can_make[i]:
            start_index = i
            while True:
                next_index = (start_index + value) % 360
                can_make[next_index] = True
                start_index = next_index
                if start_index == i:
                    break

    for i in reversed(range(360)):
        if can_make[i]:
            start_index = i
            while True:
                next_index = start_index - value
                if next_index < 0:
                    next_index += 360
                can_make[next_index] = True
                start_index = next_index
                if start_index == i:
                    break


for i in range(K):
    target = need_angle[i]
    if can_make[target]:
        print("YES")
    else:
        print("NO")