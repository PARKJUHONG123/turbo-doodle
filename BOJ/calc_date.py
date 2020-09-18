import sys

E, S, M = map(int, sys.stdin.readline().split())
e, s, m = set(), set(), set()

while True:
    e.add(E)
    s.add(S)
    m.add(M)
    E, S, M = E + 15, S + 28, M + 19
    if e & s & m:
        break

print(list(e & s & m)[0])
