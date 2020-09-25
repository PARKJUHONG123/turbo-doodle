import sys
from itertools import combinations

N, S = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
half_N = N // 2
A, B = arr[: half_N], arr[half_N :]

A_sum, B_sum = [], []
for i in range(half_N + 1):
    A_perm = combinations(A, i)
    for value in A_perm:
        value_sum = sum(value)
        A_sum.append(value_sum)

for i in range(N - half_N + 1):
    B_perm = combinations(B, i)
    for value in B_perm:
        value_sum = sum(value)
        B_sum.append(value_sum)

A_sum, B_sum = sorted(A_sum), sorted(B_sum)
A_len, B_len = len(A_sum), len(B_sum)
count, left, right = 0, 0, B_len - 1

while left < A_len and right >= 0:
    total = A_sum[left] + B_sum[right]
    if total == S:
        same_left, same_right = 0, 0
        tmp_point = left

        while left < A_len and A_sum[left] == A_sum[tmp_point]:
            same_left += 1
            left += 1

        tmp_point = right
        while right >= 0 and B_sum[right] == B_sum[tmp_point]:
            same_right += 1
            right -= 1
        count += same_left * same_right

    elif total < S:
        left += 1
    else:
        right -= 1

print(count - 1 if S == 0 else count)