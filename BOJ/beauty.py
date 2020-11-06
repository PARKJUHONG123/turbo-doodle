import sys

s = sys.stdin.readline().strip()

min_dict = dict()
max_dict = dict()
for i in range(len(s)):
    if s[i] not in max_dict:
        min_dict[s[i]] = i
        max_dict[s[i]] = i
    else:
        max_dict[s[i]] = i

keys_list = min_dict.keys()
if len(keys_list) == 1:
    print(0)
else:
    answer = 0
    for key_a in keys_list:
        for key_b in keys_list:
            value = max_dict[key_b] - min_dict[key_a]
            answer = (answer + value if value >= 0 else answer)
    print(answer)