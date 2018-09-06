# -*- coding: utf-8 -*-
"""
@author: yahia
"""

def selection_sort(Dataset):
    length = len(Dataset)
    for i in range(length):
        Min = i
        for k in range(i + 1, length):
            if Dataset[k] < Dataset[Min]:
                Min = k
        Dataset[Min], Dataset[i] = (
            Dataset[i], Dataset[Min]
        )
    return Dataset
