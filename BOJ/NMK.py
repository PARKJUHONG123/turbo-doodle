import sys
N, M, K = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, N + 1)]
ret = arr[-M : ]

s_arr = arr[: -M]
length = len(s_arr)
index = 0
if M + K - 1 <= N <= M * K:
    K = K - 1
    if K != 0:
        while True:
            if index + K < length:
                ret += s_arr[index : index + K][::-1]
                index += K
            else:
                ret += s_arr[index :][::-1]
                break
    print(*ret)
else:
    print(-1)
