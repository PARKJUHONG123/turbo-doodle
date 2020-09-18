import sys

N = int(sys.stdin.readline())
lst = [0 for _ in range(21)]

for _ in range(N):
    tmp = list(sys.stdin.readline().split())
    if len(tmp) == 1:
        command = tmp[0]
        if command == "all":
            lst = [1 for _ in range(21)]
        elif command == "empty":
            lst = [0 for _ in range(21)]
    else:
        command, num = tmp[0], int(tmp[1])
        if command == "add":
            lst[num] = 1
        elif command == "remove":
            lst[num] = 0
        elif command == "check":
            print(lst[num])
        elif command == "toggle":
            lst[num] = abs(lst[num] - 1)

