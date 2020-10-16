import sys

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()
length = len(S)

def brute(text):
    if len(text) == length:
        if text == S:
            print(1)
            exit()
        return
    if text[-1] == 'A':
        brute(text[:-1])
    elif text[-1] == 'B':
        text = text[:-1]
        brute(text[::-1])
    else:
        print(0)
        exit()

brute(T)
print(0)