import sys

N = int(sys.stdin.readline().strip())
num_arr = [0 for _ in range(10001)]

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    num_arr[num] += 1

for i in range(10001):
    for j in range(num_arr[i]):
        print(i)