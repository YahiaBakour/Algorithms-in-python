# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 18:00:53 2018

@author: yahia
"""

def DictionarySearch(A,key):
    R , L = len(A)- 1, 0
    while(R >= L):
        y = (key - A[L]) / (A[R] - A[L])
        mid = L + y * (R - L)
        mid = int(mid)
        if (A[mid] == key):
            return mid 
        if (A[mid] > key):
            R = mid - 1
        else:
            L = mid + 1
    return -1


list1 = [0,1,2,10,100,2000,10000,200000,1000000,200000000]
print("NUMBER 1000000 FOUND IN : " + str(DictionarySearch(list1,1000000)))