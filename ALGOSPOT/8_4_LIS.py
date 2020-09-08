# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 19:36:32 2020

@author: elin9
"""

A = [3, 2, 1, 7, 5, 4, 2, 6]
INF = 123456789

def lis1(A):
    if len(A) == 0:
        return 0
    ret = 0
    for i in range(len(A)):
        B = []
        for j in range(i + 1, len(A)):
            if A[i] < A[j]:
                B.append(A[j])
        ret = max(ret, 1 + lis1(B))
    return ret

n = len(A)
cache = [-1 for _ in range(n)]
def lis2(start):
    ret = cache[start]
    if ret != -1:
        return ret

    ret = 1
    for phase in range(start + 1, n):
        if A[start] < A[phase]:
            ret = max(ret, lis2(phase) + 1)
    cache[start] = ret
    return ret

def lis3(A):
    vector = [-INF]
    for i in range(n):
        if vector[-1] < A[i]:
            vector.append(A[i])
        else:
            first = 0
            last = len(vector) - 1

            while first <= last:
                mid = int((first + last) / 2)
                if A[i] < vector[mid]:
                    last = mid - 1
                elif A[i] > vector[mid]:
                    first = mid + 1
                else :
                    last = mid - 1
                    break
            vector[last + 1] = A[i]
    vector.pop(0)
    return vector

print(lis1(A))
print(lis2(0))

A = [1, 7, 3, 4, 2, 8, 5, 6, 9 ,10]
n = len(A)
print(lis3(A))