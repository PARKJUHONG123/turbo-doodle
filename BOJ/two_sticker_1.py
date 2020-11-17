import sys

H, W = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline().strip())

wall_size = H * W

sticker_dict = dict()
for i in range(N):
    R, C = map(int, sys.stdin.readline().split())
    sticker_size = R * C
    if sticker_size <= wall_size:
        if (R <= H and C <= W) or (R <= W and C <= H):
            if sticker_size in sticker_dict:
                sticker_dict[sticker_size].append([R, C])
            else:
                sticker_dict[sticker_size] = [[R, C]]
sticker_index = list(sticker_dict.keys())
length = len(sticker_index)

two_sticker_comb = dict()
for i in range(length):
    for j in range(i, length):
        if i == j:
            if len(sticker_dict[sticker_index[i]]) <= 1:
                continue
        two_sum = sticker_index[i] + sticker_index[j]
        if two_sum > wall_size:
            continue
        if two_sum in two_sticker_comb:
            two_sticker_comb[two_sum].append([sticker_index[i], sticker_index[j]])
        else:
            two_sticker_comb[two_sum] = [[sticker_index[i], sticker_index[j]]]

comb_keys = list(two_sticker_comb.keys())
comb_keys.sort(reverse = True)

def is_inside(a_sticker, b_sticker):
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
            return True

        y = ah_list[i] + bh_list[i]
        x = max(aw_list[i], bw_list[i])
        if y <= H and x <= W:
            return True
    return False

for key in comb_keys:
    for index in two_sticker_comb[key]:
        a, b = index
        if a == b:
            sticker_list = sticker_dict[a]
            inner_length = len(sticker_list)
            for i in range(inner_length):
                for j in range(i + 1, inner_length):
                    a_sticker, b_sticker = sticker_list[i], sticker_list[j]
                    if is_inside(a_sticker, b_sticker):
                        print(key)
                        exit()
        else:
            for a_sticker in sticker_dict[a]:
                for b_sticker in sticker_dict[b]:
                    if is_inside(a_sticker, b_sticker):
                        print(key)
                        exit()
print(0)