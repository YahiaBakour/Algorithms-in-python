# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 16:20:43 2018

@author: yahia
"""

def Recursive_Bubble_sort(array, is_sorted):
    if len(array) == 1 or is_sorted:
        return array
    else:
        Swapped_Flag = False
        for i in range(0,len(array)-1):
            print("Array i : " + str(array[i]))
            print("Array i + 1 : " + str(array[i+1]))
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                Swapped_Flag = True
        return Recursive_Bubble_sort(array,not Swapped_Flag)
        
List1 = [2,4,5,32,0,1,35]

print(List1)

Recursive_Bubble_sort(List1, False)

print(List1)