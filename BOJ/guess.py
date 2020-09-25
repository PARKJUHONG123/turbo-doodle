import sys

n = int(sys.stdin.readline().split()[0])
matrix = [["?" for _ in range(n)] for _ in range(n)]
tmp = sys.stdin.readline()
count = 0
for i in range(n):
    for j in range(i, n):
        matrix[i][j] = tmp[count]
        count += 1

def brute(i, j, nums):
    if j == n:
        i, j = i + 1, i + 1
        if i == n:
            print(*nums)
            exit()

    length = len(nums)
    configure = matrix[i][j]
    if i < length:
        if j < length:
            total = sum(nums[i : j + 1])
            if configure == '-':
                if total < 0:
                    brute(i, j + 1, nums)
            elif configure == '+':
                if total > 0:
                    brute(i, j + 1, nums)
            elif configure == '0':
                if total == 0:
                    brute(i, j + 1, nums)
        else:
            total = sum(nums[i:])
            for value in range(-10, 11):
                if configure == '-':
                    if total + value < 0:
                        brute(i, j + 1, nums + [value])
                elif configure == '+':
                    if total + value > 0:
                        brute(i, j + 1, nums + [value])
                elif configure == '0':
                    if total + value == 0:
                        brute(i, j + 1, nums + [value])
    else:
        for value in range(-10, 11):
            if configure == '-':
                if value < 0:
                    brute(i, j + 1, nums + [value])
            elif configure == '+':
                if value > 0:
                    brute(i, j + 1, nums + [value])
            elif configure == '0':
                if value == 0:
                    brute(i, j + 1, nums + [value])

brute(0, 0, [])