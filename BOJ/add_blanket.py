import sys

N = int(sys.stdin.readline().strip())
arr = sys.stdin.readline().strip()

def inner_calc(a, b, c):
    int_a, int_c = int(a), int(c)
    if b == '+':
        return int_a + int_c
    elif b == '-':
        return int_a - int_c
    else:
        return int_a * int_c

max_value = -sys.maxsize

def brute(index, total, condition):
    global max_value
    if index >= N:
        max_value = max(max_value, total)
        return
    if index % 2 == 0:
        int_num = int(arr[index])
        if condition == '+':
            brute(index + 1, total + int_num, None)
            if index + 3 <= N:
                inner_value = inner_calc(arr[index], arr[index + 1], arr[index + 2])
                brute(index + 3, total + inner_value, None)
            total += int(arr[index])
        elif condition == '-':
            brute(index + 1, total - int_num, None)
            if index + 3 <= N:
                inner_value = inner_calc(arr[index], arr[index + 1], arr[index + 2])
                brute(index + 3, total - inner_value, None)
        else:
            brute(index + 1, total * int_num, None)
            if index + 3 <= N:
                inner_value = inner_calc(arr[index], arr[index + 1], arr[index + 2])
                brute(index + 3, total * inner_value, None)
    else:
        brute(index + 1, total, arr[index])

brute(0, 0, '+')
print(max_value)