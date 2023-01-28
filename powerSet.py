# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 05:34:28 2022

@author: KASH

iterative implementation of power set, using binary bits of number range
from 0 to 2^(length of set). corresponding list elements are set when 
binary digits are 1 and not set when 0
complexity is O(n*2^n), the extra n factor is for extracting the bits

**note
an iterative O(2^n) stack based or recursive solution can be implemented 
without the extra n factor used in this solution
"""

def powerSet(s):
    
    num = 2**len(s)
    strSet = ""
    for x in range(num):
        print("{",end="")
        for i in range(len(s)):
            y = (x >> i) & 1
            if y:
                strSet = strSet + str(s[i]) + ","
        strSet = strSet[:len(strSet)-1]
        print(strSet + "}")
        strSet = ""
    print("Total subsets are: %d" %num)
            
        
if __name__ == '__main__':
    
    powerSet(['A','B','C','D'])
            
            
            