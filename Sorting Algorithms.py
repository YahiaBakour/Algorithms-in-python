# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 16:14:05 2018

@author: yahia
"""
def bubble_sort(Dataset):
    Len = len(Dataset)
    for i in range(Len):
        swapped = False
        for j in range(Len-1):
            if Dataset[j] > Dataset[j+1]:
                swapped = True
                Dataset[j], Dataset[j+1] = Dataset[j+1], Dataset[j]
        if not swapped: break  #Swapped Flag for O(n) time in nearly sorted
    return Dataset
