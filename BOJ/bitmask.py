import sys
A = list(map(int, sys.stdin.readline().strip()))
B = list(map(int, sys.stdin.readline().strip()))
length = len(A)
and_arr, or_arr, xor_arr = [0 for _ in range(length)], [0 for _ in range(length)], [0 for _ in range(length)]
not_A_arr, not_B_arr = [0 for _ in range(length)], [0 for _ in range(length)]

for i in range(length):
    and_arr[i] = ('1' if A[i] == B[i] == 1 else '0')
    or_arr[i] = ('1' if A[i] == 1 or B[i] == 1 else '0')
    xor_arr[i] = ('1' if A[i] + B[i] == 1 else '0')
    not_A_arr[i] = ('1' if A[i] == 0 else '0')
    not_B_arr[i] = ('1' if B[i] == 0 else '0')

print(''.join(and_arr))
print(''.join(or_arr))
print(''.join(xor_arr))
print(''.join(not_A_arr))
print(''.join(not_B_arr))
