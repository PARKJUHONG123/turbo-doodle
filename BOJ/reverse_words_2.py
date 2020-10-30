import sys
S = sys.stdin.readline().strip()

tag = list()
untag = list()
tag_plug = False
answer = list()

for i in range(len(S)):
    value = S[i]
    if value == '<':
        tag_plug = True
        answer.extend(untag[::-1])
        untag = list()
    if tag_plug:
        tag.append(value)
    else:
        if value == ' ':
            answer.extend(untag[::-1])
            answer.extend([' '])
            untag = list()
        else:
            untag.append(value)
    if value == '>':
        tag_plug = False
        answer.extend(tag)
        tag = list()

if untag:
    answer.extend(untag[::-1])
print(''.join(answer))