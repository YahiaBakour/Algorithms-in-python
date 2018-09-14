# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 18:00:53 2018

@author: yahia
"""

def DictionarySearch(A,Left,Right,key):
    if (Right >= Left):
        y = (key - A[Left]) / (A[Right] - A[Left])
        mid = Left + y * (Right - Left)
        mid = int(mid)
        if (A[mid] == key):
            return mid 
        if (A[mid] > key):
            return DictionarySearch(A, Left, mid - 1, key)
        else:
            return DictionarySearch(A, mid + 1, Right, key)
    return -1


list1 = [0,1,2,10,100,2000,10000,200000,1000000,200000000]
print("NUMBER 2000 FOUND IN : " + str(DictionarySearch(list1,0,len(list1)-1,2000)))