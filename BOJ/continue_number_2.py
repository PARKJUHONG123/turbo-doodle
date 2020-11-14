import sys

def nine_num(size):
    num = pow(10, size - 1)
    return num * 9

N, K = sys.stdin.readline().split()
K = int(K)
length = len(N)

answer = 0
for i in range(1, length):
    answer += nine_num(i) * i
num = pow(10, length - 1)
answer += (int(N) - num + 1) * length

K_temp = K
if answer < K:
    print(-1)
else:
    if length == 1:
        print(K)
    else:
        stack, size = 0, 1
        end_value = stack + size * nine_num(size)
        while True:
            if stack < K <= end_value:
                K_temp -= (stack + 1)
                outer_index = (K_temp // size)
                inner_index = (K_temp % size)
                number = str(pow(10, size - 1) + outer_index)
                print(number[inner_index])
                break
            else:
                stack = end_value
                size += 1
                end_value = stack + size * nine_num(size)