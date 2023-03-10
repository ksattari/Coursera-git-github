# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:41:29 2022

@author: KASH


"""

def findDisappearedNumbers(nums: list[int]) ->list[int]:
  
        missingNumbers = []
        maxNum = len(nums)
        nums = list(set(nums))
        nums.sort()
        expectedNumber = 1
        for i in range(maxNum):
            if i >= len(nums) and expectedNumber <= maxNum:
                missingNumbers.append(expectedNumber)
            elif i < len(nums):
                while expectedNumber != nums[i] and expectedNumber <= maxNum:
                    missingNumbers.append(expectedNumber)
                    expectedNumber += 1
            expectedNumber += 1
        return missingNumbers
        
print(findDisappearedNumbers([2,2,3,4,5,6,7,8,9,10]))
print(findDisappearedNumbers([1,1,3,4,5,6,7,10,10,10]))