import sys

sinker_num = int(sys.stdin.readline().strip())
sinker_list = list(map(int, sys.stdin.readline().split()))
sinker_list.sort(reverse = True)

bizz_num = int(sys.stdin.readline().strip())
bizz_list = list(map(int, sys.stdin.readline().split()))
max_bizz = 15000

rdp = [[False for _ in range(max_bizz + 1)] for _ in range(sinker_num + 1)]
dp = [[False for _ in range(max_bizz + 1)] for _ in range(sinker_num + 1)]
rdp[0][0], dp[0][0] = True, True

for i in range(1, sinker_num + 1):
    for j in range(max_bizz + 1):
        value = sinker_list[i - 1]
        dp[i][j] = dp[i - 1][j] or (dp[i - 1][j + value] if j + value <= max_bizz else False) or (dp[i - 1][j - value] if 0 <= j - value <= max_bizz else (rdp[i - 1][-(j - value)] if value - j <= max_bizz else False))
        rdp[i][j] = rdp[i - 1][j] or (rdp[i - 1][j + value] if j + value <= max_bizz else False) or (rdp[i - 1][j - value] if 0 <= j - value <= max_bizz else (dp[i - 1][-(j - value)] if value - j <= max_bizz else False))

result_list = list()
for i in range(bizz_num):
    flag = False
    bizz = bizz_list[i]
    if bizz > max_bizz:
        result_list.append('N')
        continue

    for j in range(sinker_num + 1):
        if dp[j][bizz]:
            result_list.append('Y')
            flag = True
            break
    if not flag:
        result_list.append('N')
print(*result_list)