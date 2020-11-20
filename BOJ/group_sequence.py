import sys

K = int(sys.stdin.readline().strip())
value = 1
while True:
    if K - value > 0:
        K -= value
        value += 1
    else:
        break
print(K)