# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 02:28:33 2018

@author: yahia
"""

import math

#Segment Tree used for getting the sum of a range in O(log n) Time 
#Also used for updating a range in O(log n) Time
class SegmentTree:
    def __init__(self,array):
        self.Length = len(array)
        #Get Height of Tree
        x = math.ceil(math.log(len(array)) / math.log(2))
        #Use height to build the max_Size of the array
        max_size = 2 * 2**x - 1
        self.SegmentTree = [0] * max_size
        self.Build_SegmentTree(array, 0, len(array) - 1,0)
        
    def MiddleIndex(self,l,r):
        return (l + r)//2
    
    def Build_SegmentTree(self,array, l , r, ci):
        if(l == r):
            self.SegmentTree[ci] = array[r]
            return array[r]
        else:
            MiddleIndex = self.MiddleIndex(l,r)
            self.SegmentTree[ci] = self.Build_SegmentTree(array,l,MiddleIndex,ci*2 + 1) + self.Build_SegmentTree(array,MiddleIndex + 1,r,ci*2 + 2)
            return self.SegmentTree[ci]
        

    def Query_Get_Sum_Utility(self,li, ri, sq, eq, ci):
        if(sq <= li and eq >= ri):
            return self.SegmentTree[ci]
        if (ri < sq or li > eq):
            return 0
        else:
            MiddleIndex = self.MiddleIndex(li,ri)
            return self.Query_Get_Sum_Utility(li, MiddleIndex, sq, eq, ci*2 + 1) + self.Query_Get_Sum_Utility(MiddleIndex+1,ri , sq, eq, ci*2 + 2)
        
    def Query_Get_Sum(self, l , r):
       if(l < 0 or  r > self.Length-1 or l > r):
           print("Invalid Input, Please Query Correctly : ")
           return -1
       else:
           return self.Query_Get_Sum_Utility(0,self.Length - 1, l, r,0)
       
    def UpdateValue(self,array, index, newVal):
        if(index < 0 or index > len(array) - 1):
            print("Invalid Input, Get your act together")
            return -1
        difference = newVal - array[index]
        array[index] = newVal
        self.UpdateValueUtility(0,len(array)-1,index,difference,0)
        
    def UpdateValueUtility(self,li,ri, index, difference, ci):
        if(index < li or index > ri):
            return
        self.SegmentTree[ci] += difference
        if(li != ri):
            MiddleIndex = self.MiddleIndex(li,ri)
            self.UpdateValueUtility(li, MiddleIndex,index, difference, 2*ci + 1)
            self.UpdateValueUtility(MiddleIndex + 1, ri,index, difference, 2*ci + 2)
            
        
    def printTreeData(self):
        for i in self.SegmentTree:
            print( str(i) + " :  ", end = "")
       
       
List1 = [1,2,3,4,5,6,7,8,9,10]

T1 = SegmentTree(List1)

print(T1.Query_Get_Sum(0,3))

NewVal = 10
print("Updating First Value from :  " + str(List1[0]) + " to : " + str(NewVal))
T1.UpdateValue(List1,0,10)

print(T1.Query_Get_Sum(0,3))



