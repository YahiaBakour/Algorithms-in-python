# -*- coding: utf-8 -*-
"""
@author: yahia
"""


def insertion_sort(Dataset):
    for i in range(1, len(Dataset)):
        while 0 < i and Dataset[i] < Dataset[i - 1]:
            Dataset[i], Dataset[
                i - 1] = Dataset[i - 1], Dataset[i]
            i -= 1
    return Dataset
