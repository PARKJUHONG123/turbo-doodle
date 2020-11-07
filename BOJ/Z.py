import sys
N, r, c = map(int, sys.stdin.readline().split())
n = N
length = 2 ** (n - 1)
order = 0

def search_order(length, r, c):
    global order
    for i in range(2):
        for j in range(2):
            height, width = i * length, j * length
            if height <= r < height + length:
                if width <= c < width + length:
                    inner_order = 2 * i + j
                    order += inner_order * (length ** 2)
                    if not (r == height and c == width):
                        search_order(length // 2, r - height, c - width)
search_order(length, r, c)
print(order)
