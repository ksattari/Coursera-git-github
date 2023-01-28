# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:19:33 2022

@author: Khashayar Sattari

implementation of merge-sort 
input: unsorted list of integers or floats
output : returns sorted list of original list elements
time complexity: O(nlogn)
space complexity: O(n)

merge part of merge-sort
input: left, right sorted lists, optional: comparator function
output: merged sorted list combining left and right
"""
def merge(left,right,f = None):
     
    i,j = 0,0
    mergedList = []
    while i < len(left) and j < len(right):
        comp = left[i]-right[j] if f == None else f(left[i],right[j])
        if comp < 0:
            mergedList.append(left[i])
            i += 1
        else:
            mergedList.append(right[j])
            j += 1
    while i < len(left):
        mergedList.append(left[i])
        i += 1
    while j < len(right):
        mergedList.append(right[j])
        j += 1
    return mergedList 
            
"""
main recursive function of merge-sort to divide lists into left, right
then call mergesort on them recursively, returning the merge of both lists
input: list of numbers, optional: comparator function
output : returns sorted list of numbers
"""
def mergesort(unsorted,f = None):
    
    if len(unsorted) == 1:
        return unsorted
    mid = len(unsorted) // 2
    sortedLeft = mergesort(unsorted[0:mid],f)
    sortedRight = mergesort(unsorted[mid:len(unsorted)],f)
    return merge(sortedLeft,sortedRight,f)

if __name__ == '__main__':
    
    f = lambda b,a: a-b
    print(mergesort([4,6,3,2,1]))
    print(mergesort([1],f))
    print(mergesort([2,2,2],f))
    print(mergesort([4,3,2,100,1],f))
    print(mergesort([23,89,67,66,56,9,35,21,59,92,15,48,95,78,65,80,30,22,10,34,39
                     ,46,88,38,99,7,12,68,57,8,85,11,27,62,69,25,43,1,44,47,2
                     ,96,26,40,93,58,70,6,100,75,71,52,54,42,64,32,33,13
                     ,79,55,51,83,84,41,97,5,91,29,14,90,18,61,86
                     ,73,19,77,82,63,24,31,50,94,36,4,16,72,20,37,98,53
                     ,87,76,49,60,81,74,45,28,17,3],f))


    