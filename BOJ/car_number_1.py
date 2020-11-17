import sys

alpha_width = 26
number_width = 10

arr = sys.stdin.readline().strip()
length = len(arr)

def return_width(value):
    if value == 'c':
        return alpha_width
    else:
        return number_width

if length == 0:
    print(0)

elif length == 1:
    if arr[0] == 'd':
        print(number_width)
    else:
        print(alpha_width)
else:
    total_count = return_width(arr[0])
    stance = arr[0]
    for i in range(1, length):
        if arr[i] == stance:
            total_count *= (return_width(stance) - 1)
        else:
            total_count *= return_width(arr[i])
            stance = arr[i]
    print(total_count)