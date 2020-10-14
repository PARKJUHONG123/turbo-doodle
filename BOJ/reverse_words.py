import sys

N = int(sys.stdin.readline())

for _ in range(N):
    ret = ""
    words = sys.stdin.readline().split()
    for value in words:
        value = (list(reversed(value)))
        ret += "".join(value)
        ret += " "
    print(ret[:-1])
