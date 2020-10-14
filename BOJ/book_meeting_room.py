import sys

N = int(sys.stdin.readline())

book_dict = dict()
max_num = -1
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if b in book_dict:
        book_dict[b].append(a)
    else:
        book_dict[b] = [a]

for key in book_dict.keys():
    book_dict[key].sort()
book_dict = sorted(book_dict.items(), key = lambda x:x[0])
count = 0
last_end = -1
for i in range(len(book_dict)):
    end, start_list = book_dict[i][0], book_dict[i][1]

    for start in start_list:
        if last_end <= start:
            last_end = end
            print(start, end)
            count += 1
print(count)