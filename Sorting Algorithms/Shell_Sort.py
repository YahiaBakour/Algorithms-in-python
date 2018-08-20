#!/usr/bin/python
# -*- coding: utf-8 -*-


def shellsort(arr):
    arrlength = len(arr)
    gap = 1
    #Knuths Formula
    while (gap <= arrlength /3):
        gap = gap * 3 + 1
        
    while gap > 0:
        for i in range(gap,len(arr)):
        #Select Value to be inserted
            valuetobeinserted = arr[i]
            j = i
        #Shift element towards right
            while j >= gap and arr[j - gap] > valuetobeinserted:
                arr[j] = arr[j - gap]
                j -= gap
        #Insert number
            arr[j] = valuetobeinserted
        #Recalculate Interval
        gap  = (gap - 1)// 3



			
  
			
List1 = [-532,532,502,20,0,21,2,3,4,1]

print(List1)
shellsort(List1)
print(List1)