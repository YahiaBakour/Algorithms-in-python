# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 18:00:53 2018

@author: yahia
"""

def Bsearch(Arr, Left, Right, Key):
    if (Right >= Left) :
        mid = (Left + Right-1)//2; # Find Middle
        if (Arr[mid] == Key):
            return mid 
        if (Arr[mid] > Key):
            return Bsearch(Arr, Left, mid-1, Key)
        else:
            return Bsearch(Arr, mid+1, Right, Key)
    return -1


list1 = [0,1,2,10,100,2000,10000,200000,1000000,200000000]
print("NUMBER 100 FOUND IN : " + str(Bsearch(list1,0,len(list1)-1,100)))