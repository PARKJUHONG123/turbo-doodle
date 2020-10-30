import sys

N = int(sys.stdin.readline().strip())

def valid_configure(arr):
    for value in arr:
        if value == '(':
            input_list.append(value)
        else:
            if not input_list:
                return False
            input_list.pop()
    if input_list:
        return False
    return True

for _ in range(N):
    arr = sys.stdin.readline().strip()
    input_list = list()
    print("YES" if valid_configure(arr) else "NO")
