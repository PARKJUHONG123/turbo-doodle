import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
plus, minus, mult, div = list(map(int, sys.stdin.readline().split()))

min_value, max_value = 987654321, -987654321

def brute(nums, index, total, plus, minus, mult, div):
    global min_value, max_value
    if index >= N:
        if total > max_value:
            max_value = total
        if total < min_value:
            min_value = total
        return

    if index == 0:
        brute(nums, index + 1, nums[index], plus, minus, mult, div)

    else:
        if plus > 0:
            brute(nums, index + 1, total + nums[index], plus - 1, minus, mult, div)

        if minus > 0:
            brute(nums, index + 1, total - nums[index], plus, minus - 1, mult, div)

        if mult > 0:
            brute(nums, index + 1, total * nums[index], plus, minus, mult - 1, div)

        if div > 0:
            if total >= 0:
                tmp = total // nums[index]
            else:
                tmp = -(abs(total) // nums[index])
            brute(nums, index + 1, tmp, plus, minus, mult, div - 1)

brute(nums, 0, 0, plus, minus, mult, div)
print(max_value)
print(min_value)