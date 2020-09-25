import sys

N = sys.stdin.readline()[:-1]

N_list = []
for i in range(len(N)):
    N_list.append(int(N[i]))

N = int(N)
nature = abs(N - 100)

length = len(N_list)
M = int(sys.stdin.readline())
WB = list(map(int, sys.stdin.readline().split()))
B = []

for i in range(10):
    if i not in WB:
        B.append(str(i)) # 2 8

if len(B) == 0:
    print(nature)
    exit()

min_cnt = nature
check_over = False
for num in range(1000001):
    num = str(num)
    for j in range(len(num)):
        if num[j] not in B:
            break
        elif j == len(num) - 1:
            min_cnt = min(min_cnt, abs(N - int(num )) + len(str(num)))
print(min_cnt)
