# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 06:44:53 2022

@author: KASH
"""

def fibonacci(n):
    
    fNMinus2 = 0 
    fNMinus1 = 1
    fN = 0 if n == 0 else 1
    for i in range(1,n):
        fN = fNMinus1 + fNMinus2
        fNMinus2 = fNMinus1
        fNMinus1 = fN
    return fN

if __name__ == '__main__':
    
    print(fibonacci(37))
        
    