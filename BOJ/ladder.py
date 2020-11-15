import sys
import math
x, y, c = map(float, sys.stdin.readline().split())
low, high = 0, min(x, y)

while low <= high:
    mid = (low + high) / 2
    x_height = math.sqrt(x ** 2 - mid ** 2)
    y_height = math.sqrt(y ** 2 - mid ** 2)
    y_width = (c / y_height) * mid
    x_width = (c / x_height) * mid

    if c / y_height + c / x_height <= 1:
        low = mid + 0.0001
    else:
        high = mid - 0.0001
print(format(high, ".3f"))