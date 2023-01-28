# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 19:41:18 2022

@author: KASH
"""
def findDisappearedNumbers(nums: list[int]) -> list[int]:
    
    lookupArray = [0] * (len(nums) + 1)
    missingNumbers = []
    for i in range(len(nums)):
        lookupArray[nums[i]] = 1
    for i in range(1,len(lookupArray)):
        if lookupArray[i] == 0:
            missingNumbers.append(i)
    return missingNumbers
    
    
    
print(findDisappearedNumbers([2,2,3,4,5,6,7,8,9,10]))
print(findDisappearedNumbers([1,1,3,4,5,6,7,10,10,10]))