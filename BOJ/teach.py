import sys
from itertools import combinations

input = sys.stdin.readline

N, K = list(map(int, input().split()))
a_value = ord('a')

have_to_study = ['a', 'c', 'n', 'i', 't']

if K < 5:
    print(0)
    exit()
K = K - 5

word_list = []
whole_words = set()
for _ in range(N):
    read = input()
    word = []
    for i in range(4, len(read) - 5):
        if read[i] not in have_to_study:
            word.append(ord(read[i]) - a_value)
    word = set(word)
    whole_words |= word
    word_list.append(word)

max_count = 0
if len(whole_words) < K:
    print(N)
else:
    comb = combinations(whole_words, K)
    for value in comb:
        count = 0
        value = set(value)
        for word in word_list:
            result = word - value
            if not result:
                count += 1
        max_count = max(max_count, count)
    print(max_count)