import sys

N = int(sys.stdin.readline().strip())
card_dict = dict()

for _ in range(N):
    card = int(sys.stdin.readline().strip())
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1

max_num, max_key = -1, -1
for key in card_dict.keys():
    if card_dict[key] > max_num:
        max_num = card_dict[key]
        max_key = key

    elif card_dict[key] == max_num:
        if key < max_key:
            max_key = key
print(max_key)