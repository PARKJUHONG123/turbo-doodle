import sys

alpha_list = []
a_num, A_num = ord('a'), ord('A')
for i in range(26):
    alpha_list.append(chr(a_num + i))
    alpha_list.append(chr(A_num + i))
sentence = sys.stdin.readline().split()
length = len(sentence)
base = sentence[0]

not_declared = [',', ' ', ';']
for i in range(1, length):
    output = base
    value = sentence[i]
    alpha_word = ""
    stack = []
    for alpha in value:
        if alpha in alpha_list:
            alpha_word += alpha
        else:
            if alpha not in not_declared:
                stack.append(alpha)
    while stack:
        a = stack.pop()
        if a == ']':
            b = stack.pop()
            output += (b + a)
        else:
            output += a

    output += " " + alpha_word + ";"
    print(output)
