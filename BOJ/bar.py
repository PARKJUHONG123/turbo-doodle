import sys
X = int(sys.stdin.readline())
bar_list = [64]

while True:
    if sum(bar_list) > X:
        min_bar = bar_list.pop()
        half_bar = min_bar // 2
        sum_bar = sum(bar_list)
        if half_bar + sum_bar >= X:
            bar_list.append(half_bar)
        else:
            bar_list.append(half_bar)
            bar_list.append(half_bar)
    else:
        print(len(bar_list))
        break