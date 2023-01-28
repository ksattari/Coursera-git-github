# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 05:05:23 2022

@author: KASH
"""

def findDisappearedNumbers(nums: list[int]) -> list[int]:
 
        missingNumbers = []
        for i in range(len(nums)):
            index = nums[i]-1
            if index == i:
                pass
            else:
                missingNumbers.append(nums[index])
                nums[index] = nums[i]
        while missingNumbers:
            num = missingNumbers.pop()
            nums[num-1] = num
        for x in range(len(nums)):
            if nums[x] != x+1:
                missingNumbers.append(x+1)
        return missingNumbers

print(findDisappearedNumbers([2,2,3,4,5,6,7,8,9,10]))
print(findDisappearedNumbers([1,1,3,4,5,6,7,10,10,10]))