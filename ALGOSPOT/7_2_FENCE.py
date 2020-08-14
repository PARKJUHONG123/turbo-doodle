# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:59:58 2020

@author: elin9
"""

def biggest_rectangle(left, right):
    if left == right:
        return fences[left]
    
    mid = int((left + right) / 2)
    ret = max(biggest_rectangle(left, mid), biggest_rectangle(mid + 1, right))
    
    lo = mid
    hi = mid + 1
    height = min(fences[lo], fences[hi])
    ret = max(ret, height * 2)
    
    while (left < lo or right > hi):
        if hi < right and (lo == left or fences[lo - 1] < fences[hi + 1]):
            hi += 1
            height = min(height, fences[hi])
        else:
            lo -= 1
            height = min(height, fences[lo])
    
        ret = max(ret, height * (hi - lo + 1))
    return ret

def find_widest(fences, height, fence_num):
    ret_num = 0; count = 0
    for i in range(fence_num):
        if fences[i] >= height:
            if count == 0:
                count = 1
            else:
                if fences[i - 1] >= height:
                    count += 1
                else :
                    count = 1
        ret_num = max(ret_num,count)
    return ret_num

file = open("7_2_input.txt", "r")
C = int(file.readline())
for _ in range(C):
    fence_num = int(file.readline())
    fences = list(map(int, file.readline().split()))
    highest = max(fences)
    
    # O(n^2)
    area = [0 for _ in range(highest + 1)]
    for i in reversed(range(highest + 1)):
        area[i] = find_widest(fences, i, fence_num) * i
    print("O(n^2) : " + str(max(area)))

    # O(n*log(n))
    print("O(n * log(n)) : " + str(biggest_rectangle(0, fence_num - 1)))
    