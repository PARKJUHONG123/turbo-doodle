import sys
import copy
N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

num_count_dict = dict()
num_count = len(arr)
for value in arr:
    if value in num_count_dict:
        num_count_dict[value] += 1
    else:
        num_count_dict[value] = 1
num_set = list(num_count_dict.keys())

def brute(num, left_count, visited):
    if left_count == 0:
        print(*visited)
        return

    div_value = num // 3
    if div_value * 3 == num:
        if div_value in left_count_dict:
            if left_count_dict[div_value] > 0:
                left_count_dict[div_value] -= 1
                brute(div_value, left_count - 1, visited + [div_value])
                left_count_dict[div_value] += 1

    mult_value = num * 2
    if mult_value in left_count_dict:
        if left_count_dict[mult_value] > 0:
            left_count_dict[mult_value] -= 1
            brute(mult_value, left_count - 1, visited + [mult_value])
            left_count_dict[mult_value] += 1

for num in num_set:
    left_count_dict = copy.deepcopy(num_count_dict)
    left_count = num_count
    brute(num, left_count - 1, [num])
