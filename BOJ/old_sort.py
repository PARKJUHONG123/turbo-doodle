import sys

N = int(sys.stdin.readline().strip())

age_dict = dict()
for _ in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)

    if age in age_dict:
        age_dict[age].append(name)
    else:
        age_dict[age] = [name]

key_list = list(age_dict.keys())
key_list.sort()

for key in key_list:
    for value in age_dict[key]:
        print(key, end = ' ')
        print(value)
