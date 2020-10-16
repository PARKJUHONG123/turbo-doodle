import sys

N = int(sys.stdin.readline())
plus_arr, minus_arr = list(), list()

for _ in range(N):
    value = int(sys.stdin.readline())
    if value > 0:
        plus_arr.append(value)
    else:
        minus_arr.append(value)
plus_arr.sort(reverse = True)
minus_arr.sort()

len_plus, len_minus = len(plus_arr), len(minus_arr)

plus_index, plus_total, left_plus = 0, 0, -1
if len_plus % 2 == 0:
    while plus_index < len_plus:
        a, b = plus_index, plus_index + 1
        plus, mult = plus_arr[a] + plus_arr[b], plus_arr[a] * plus_arr[b]
        plus_total += max(plus, mult)
        plus_index += 2

else:
    left_plus = plus_arr[-1]
    len_plus -= 1
    while plus_index < len_plus:
        a, b = plus_index, plus_index + 1
        plus, mult = plus_arr[a] + plus_arr[b], plus_arr[a] * plus_arr[b]
        plus_total += max(plus, mult)
        plus_index += 2

minus_index, minus_total, left_minus = 0, 0, 1
if len_minus % 2 == 0:
    while minus_index < len_minus:
        a, b = minus_index, minus_index + 1
        plus, mult = minus_arr[a] + minus_arr[b], minus_arr[a] * minus_arr[b]
        minus_total += max(plus, mult)
        minus_index += 2

else:
    left_minus = minus_arr[-1]
    len_minus -= 1
    while minus_index < len_minus:
        a, b = minus_index, minus_index + 1
        plus, mult = minus_arr[a] + minus_arr[b], minus_arr[a] * minus_arr[b]
        minus_total += max(plus, mult)
        minus_index += 2

total = 0
if left_minus == 1:
    if left_plus == -1:
        total = minus_total + plus_total
    else:
        total = minus_total + plus_total + left_plus

else:
    if left_plus == -1:
        total = minus_total + plus_total + left_minus

    else:
        total = minus_total + plus_total + max(left_minus * left_plus, left_minus + left_plus)
print(total)