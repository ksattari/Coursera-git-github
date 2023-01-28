# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 14:08:51 2022

@author: KASH
"""

def sortedSquares(nums: list[int]) -> list[int]:
    
    #O(n) solution using merging two sorted halves
    squares = []
    #find split point between negative and positive
    split = 0
    while split < len(nums) and nums[split] < 0:
        split += 1
    # merge two parts after squaring and comparing the values
    i = split - 1 #left half index
    j = split     #right half index
    while i >= 0 and j < len(nums):
        if abs(nums[i]) > abs(nums[j]):
            squares.append(nums[j]**2)
            j+=1
        else:
            squares.append(nums[i]**2)
            i-=1
    while j < len(nums):
        squares.append(nums[j] ** 2)
        j +=1
    while i >= 0:
        squares.append(nums[i]**2)
        i -= 1
    return squares
    
if __name__ == '__main__':
    
    print(sortedSquares([-4,-1,0,3,10]))
    print(sortedSquares([-4,-1]))