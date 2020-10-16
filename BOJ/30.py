import sys

num = sys.stdin.readline().strip()

if '0' not in num:
    print(-1)
else:
    total = 0
    arr = []
    for i in range(len(num)):
        number = int(num[i])
        total += number
        arr.append(number)
    if total % 3 == 0:
        arr.sort(reverse = True)
        ret = 0
        for value in arr:
            ret *= 10
            ret += value
        print(ret)
    else:
        print(-1)