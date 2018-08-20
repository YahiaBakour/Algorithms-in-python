# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 07:18:30 2018

@author: yahia
"""
class FenwickTree:
    def __init__(self, array):
        self.Size = len(array)
        self.FenwickTree = [0] * (len(array)+1)
        self.ConstructFT(array)
        
    def UpdateBit(self, i, val): 
        i += 1
        while (i <= self.Size):
            self.FenwickTree[i] += val
            i += i & (-i)

    def query(self, i): 
        i +=1
        result = 0
        while (i > 0):
            result += self.FenwickTree[i]
            i -= i & (-i)
        return result
    
    def ConstructFT(self,array):
        for i in range(self.Size):
            self.UpdateBit(i,array[i])
        return self.FenwickTree
    
List1 = [0,1,2,3,4,5,6,7,8,9,10]
FT1 = FenwickTree(List1)
print(FT1.query(5))