# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 03:21:31 2018

@author: yahia
"""
 
def pancakeSort(arr, n):
    Current_Stack = n
    while Current_Stack > 1:
        mi = arr[:Current_Stack].index(max(arr[:Current_Stack]))
        if mi != Current_Stack-1:
            arr[:mi+1] = arr[:mi+1][::-1]
            arr[:Current_Stack] = arr[:Current_Stack][::-1]
        Current_Stack -= 1
        
List1 = [23,432,52,25,12,0,1]
print(List1)
pancakeSort(List1,len(List1))
print(List1)