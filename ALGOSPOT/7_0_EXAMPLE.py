# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:32:03 2020

@author: elin9
"""

import random

class sum_class:
    # 1~n sum
    def fast_sum(self, n):
        if n == 1:
            return 1
        if n % 2 == 1:
            return self.fast_sum(n-1) + n
        return 2 * self.fast_sum(n/2) + (n/2) *(n/2)
    
    def __main__(self, n):
        print(int(self.fast_sum(n)))

class square_matrix:
    # A == n*n matrix
    # A^m = A^(m/2) * A^(m/2)

    def identity(self, n):
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            self.matrix[i][i] = 1    
        return self.matrix
    
    def pow_function(self, matrix_a, matrix_b, n):
        ret_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    ret_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
        return ret_matrix

    def pow_matrix(self, matrix, m, n):
        if m == 0:
            return self.identity(n)
        if m % 2 > 0:
            return self.pow_function(self.pow_matrix(matrix, m - 1, n), matrix, n)
        
        half_matrix = self.pow_matrix(matrix, m/2, n)
        return self.pow_function(half_matrix, half_matrix, n)

    def __main__(self, size):
        matrix = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                matrix[i][j] = random.randint(0, 10)
        print(matrix)
        print(self.pow_matrix(matrix, 2, size))


class quick_class:
    def partition(self, array, left, right):
        low = left
        high = right
        pivot = array[left]
        
        while low < high:
            # continue while elements do not need to be compared
            while low <= right and array[low] < pivot:
                low += 1
            while high >= left and array[high] > pivot:
                high -= 1
            
            # if array[low] is bigger than array[high]
            # swap each elements
            if low < high :
                temp = array[low]
                array[low] = array[high]
                array[high] = temp
        
        # left ~ high : all values are smaller than pivot
        # high ~ right : all values are bigger than pivot
        return array, high

    def quick_sort(self, array, left, right):
        if left < right:
            array, pivot = self.partition(array, left, right)            
            array = self.quick_sort(array, left, pivot - 1)
            array = self.quick_sort(array, pivot + 1, right)
        return array
    
    def __main__ (self):
        array = [38, 27, 43, 9, 3, 82, 10]
        print(self.quick_sort(array, 0, len(array) - 1))


class merge_class:
    def merge(self, array, left, mid, right):
        first_array_index = left
        second_array_index = mid + 1
        temp_array_index = left
        temp_array = [0 for _ in range(len(array))]
        
        while first_array_index <= mid and second_array_index <= right:
            # while there are some elements in first array and second array
            # compare elements and insert into temp array orderly
            if array[first_array_index] <= array[second_array_index]:
                temp_array[temp_array_index] = array[first_array_index]                
                first_array_index += 1
            else:
                temp_array[temp_array_index] = array[second_array_index]
                second_array_index += 1
            temp_array_index += 1
                
        if first_array_index > mid:
            # if there is no more elements in first array
            # copy second array into temp array
            for l in range(second_array_index, right + 1):
                temp_array[temp_array_index] = array[l]
                temp_array_index += 1
        else :
            # if there is no more elements in second array
            # copy first array into temp array
            for l in range(first_array_index, mid + 1):
                temp_array[temp_array_index] = array[l]
                temp_array_index += 1
  
        for l in range(left, right + 1):
            # array has not-ranged elements
            # temp array has ranged ordered elements
            # so insert ranged ordered elements into return array
            array[l] = temp_array[l]

        return array
            
    def merge_sort(self, array, left, right):
        if left < right:
            mid = int((left + right) / 2)
            array = self.merge_sort(array, left, mid)
            array = self.merge_sort(array, mid + 1, right)
            array = self.merge(array, left, mid, right)
        return array

    def __main__ (self):
        array = [38, 27, 43, 9, 3, 82, 10]
        print(self.merge_sort(array, 0, len(array) - 1))
    
class big_multiplication:
    
    def normalize(self, num_array):
        num_array.append(0)
        for i in range(len(num_array) - 1):
            if num_array[i] < 0:
                borrow = int((abs(num_array[i]) + 9) / 10)
                num_array[i + 1] -= borrow
                num_array[i] += borrow * 10
            else:
                num_array[i + 1] += int(num_array[i] / 10)
                num_array[i] %= 10
        
        while (len(num_array) > 1 and num_array[-1] == 0):
            num_array.pop()
    
    def multiply(self, a, b):
        c = [0 for _ in range(len(a) + len(b) + 1)]
        for i in range(len(a)):
            for j in range(len(b)):
                c[i + j] += a[i] * b[j]
                
        self.normalize(c)
        return c
    
    def num_to_array(self, num):
        if num == 0:
            return [0]
        
        decimal = 10
        ret_array = []
        while(num != 0):
            ret_array.append(int(num % decimal))
            num /= decimal
            num = int(num)
        return ret_array
    
    def array_to_num(self, array):
        ret_num = 0
        while(True):
            ret_num += array[-1]
            array.pop()
            if len(array) == 0:
                return ret_num
            ret_num *= 10        
        
    def __main__(self):
        a = self.num_to_array(123)
        b = self.num_to_array(456)
        print(self.array_to_num(self.multiply(a, b)))

example1 = sum_class()
example1.__main__(10)

example2 = square_matrix()
example2.__main__(3)

example3 = quick_class()
example3.__main__()

example4 = merge_class()
example4.__main__()

example5 = big_multiplication()
example5.__main__()