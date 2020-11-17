import sys
roman = [1, 5, 10, 50]
N = int(sys.stdin.readline().strip())

num_set = set()
for number in roman:
    num_set.add(number)

for i in range(1, N):
    next_set = set()
    for value in num_set:
        for number in roman:
            next_set.add(number + value)
    num_set = next_set

print(len(num_set))