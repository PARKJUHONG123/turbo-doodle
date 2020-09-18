import sys
import math

lst = []
while True:
    value = int(sys.stdin.readline())
    if value == 0:
        break
    lst.append(value)

max_value = max(lst)
prime = [True for _ in range(max_value + 1)]
mv_sqrt = int(math.sqrt(max_value))

if pow(mv_sqrt, 2) == max_value:
    pass
else:
    mv_sqrt += 1

prime[0], prime[1] = False, False
for i in range(2, mv_sqrt + 1):
    for j in range(2, max_value):
        index = i * j
        if index > max_value:
            break
        if prime[index]:
            prime[index] = False

for value in lst:
    token = False
    for i in range(len(prime)):
        if i > value:
            break
        if prime[i]:
            if prime[(value - i)]:
                print(value, end=" = ")
                print(i, end=" + ")
                print(value - i)
                token = True
                break
    if token == False:
        print("Goldbach's conjecture is wrong.")
