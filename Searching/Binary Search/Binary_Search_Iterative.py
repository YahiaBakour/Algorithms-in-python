# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 18:00:53 2018

@author: yahia
"""

def Bsearch(Arr,key): 
    R,L = len(Arr)-1,0
    while(R >= L):
        mid = (L + R -1)//2;
        if (Arr[mid] == key):
            return mid
        if (Arr[mid] > key):
            R = mid - 1
        else:
            L = mid + 1
    return -1

list1 = [0,1,2,10,100,2000,10000,200000,1000000,200000000]
print("NUMBER 100 FOUND IN : " + str(Bsearch(list1,100)))