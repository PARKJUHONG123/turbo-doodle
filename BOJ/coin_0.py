import sys

N, K = map(int, sys.stdin.readline().split())
coin_list = [0 for _ in range(N)]

for i in range(N):
    coin_list[i] = (int(sys.stdin.readline()))
coin_list.reverse()

left, index, count = K, 0, 0
while index < N:
    if coin_list[index] <= left:
        inner_count = left // coin_list[index]
        left %= coin_list[index]
        count += inner_count
        if left == 0:
            break
    else:
        index += 1
print(count)