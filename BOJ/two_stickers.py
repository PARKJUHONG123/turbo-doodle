import sys

H, W = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline().strip())
sticker_list = []
max_dimension = 0
stack = list()

def calc_dimension(a_sticker, b_sticker):
    global max_dimension
    ax, ay = a_sticker
    bx, by = b_sticker
    aw_list = [ax, ax, ay, ay]
    ah_list = [ay, ay, ax, ax]
    bw_list = [bx, by, bx, by]
    bh_list = [by, bx, by, bx]

    for i in range(4):
        y = max(ah_list[i], bh_list[i])
        x = aw_list[i] + bw_list[i]
        if y <= H and x <= W:
            max_dimension = max(ah_list[i] * aw_list[i] + bh_list[i] * bw_list[i], max_dimension)

        y = ah_list[i] + bh_list[i]
        x = max(aw_list[i], bw_list[i])
        if y <= H and x <= W:
            max_dimension = max(ah_list[i] * aw_list[i] + bh_list[i] * bw_list[i], max_dimension)


for i in range(N):
    R, C = map(int, sys.stdin.readline().split())
    sticker_list.append([R, C])

for i in range(N):
    for j in range(i + 1, N):
        calc_dimension(sticker_list[i], sticker_list[j])
print(max_dimension)
