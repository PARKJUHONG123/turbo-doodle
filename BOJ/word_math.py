import sys
N = int(sys.stdin.readline())
num = [[] for _ in range(8)]

for _ in range(N):
    tmp = list(reversed(sys.stdin.readline().split()[0]))
    for i in range(len(tmp)):
        num[i].append(tmp[i])

importance = dict()
for i in range(len(num)):
    for value in num[i]:
        if value not in importance:
            importance[value] = pow(10, i)
        else:
            importance[value] += pow(10, i)
importance = (sorted(importance.items(), key = (lambda x : x[1]), reverse = True))
point = 9
alpha = dict()
for value in importance:
    alpha[value[0]] = point
    point -= 1

total = 0
for i in range(len(num)):
    ret = 0
    for value in num[i]:
        ret += alpha[value]
    ret *= pow(10, i)
    total += ret

print(total)