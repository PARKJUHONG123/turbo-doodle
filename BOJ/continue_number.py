# 1~9 : 9
# 10~99 : 90
# 100~999 : 900
# 1000~9999 : 9000

import sys

def nine_num(size):
    num = pow(10, size - 1)
    return num * 9

N = sys.stdin.readline().split()[0]
length = len(N)
answer = 0
for i in range(1, length):
    answer += nine_num(i) * i
num = pow(10, length - 1)
answer += (int(N) - num + 1) * length
print(answer)