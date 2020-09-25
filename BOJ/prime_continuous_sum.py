import sys
import math
N = int(sys.stdin.readline().split()[0])

def prime(N):
    if N == 1:
        return []
    elif N == 2:
        return [2]
    else:
        primes = [True for _ in range(N + 1)]
        primes[0], primes[1] = False, False

        value = int(math.sqrt(N))
        if value * value == N:
            end = value + 1
        else:
            end = value

        for i in range(2, end):
            if primes[i]:
                for j in range(i * 2, N + 1, i):
                    primes[j] = False
        primes_list = []
        for i in range(N + 1):
            if primes[i]:
                primes_list.append(i)
        return primes_list

M = N
arr = prime(N)
N = len(arr)
if N == 0:
    print(0)
    exit()

start, end = 0, 0
count = 0
total = arr[start]


while True:
    if start <= end < N:
        if total == M:
            count += 1
            end += 1
            if end < N:
                total += arr[end]
        elif total < M:
            end += 1
            if end < N:
                total += arr[end]
        elif total > M:
            total -= arr[start]
            start += 1
    else:
        if end < start <= N:
            end += 1
            if end < N:
                total += arr[end]
            continue
        if end == N:
            if start == N:
                break
            else:
                while start < N:
                    total -= arr[start]
                    if total == M:
                        count += 1
                    start += 1
print(count)