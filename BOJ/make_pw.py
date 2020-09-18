import sys
from itertools import combinations

n, m = list(map(int, sys.stdin.readline().split()))
word = sys.stdin.readline().split()
word.sort()

comb_list = list(combinations(word, n))

def check_word(word):
    b = [0 for _ in range(5)]
    b[0] = word.count('a')
    b[1] = word.count('e')
    b[2] = word.count('i')
    b[3] = word.count('o')
    b[4] = word.count('u')

    b_total = sum(b)
    a_total = len(word) - b_total

    if b_total >= 1 and a_total >= 2:
        return True
    return False

for value in comb_list:
    if check_word(value):
        print("".join(value))
