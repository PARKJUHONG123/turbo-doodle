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

    if text[0] == 'B':
        left = text[1:]
        brute(left[::-1])
    if text[-1] == 'A':
        left = text[:-1]
        brute(left)


brute(T)
print(0)