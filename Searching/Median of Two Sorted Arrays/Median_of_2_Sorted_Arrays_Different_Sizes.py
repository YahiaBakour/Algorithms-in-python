# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 19:45:00 2018

@author: Yahia Bakour, OOG
"""

def find_Median(A,B):
    if(len(A) > len(B)):
        Arr1 , n = B, len(B)
        Arr2 , m = A, len(A)
    else:
        Arr1 , n = A, len(A)
        Arr2 , m = B, len(B)
    
    Min, Max = 0 , n
    while(Min <= Max):
        #Setting Partitions
        Partition_1 = (Min + Max) // 2
        Partition_2 = (n + m + 1) // 2 - Partition_1
        
        #For maxleft1
        if(Partition_1 != 0):
            Max_Left_1 = Arr1[Partition_1 - 1]
        else:
            Max_Left_1 = float("-inf")

        #For minRight1
        if(Partition_1 != n):
            Min_Right_1 = Arr1[Partition_1]
        else:
            Min_Right_1 = float("inf")
            
        #For maxLeft2
        if(Partition_2):
            Max_Left_2 = Arr2[Partition_2 - 1]
        else:
            Max_Left_2 = float("-inf")  
        
        #For MinRight2
        if(Partition_2 != m):
            Min_Right_2 = Arr2[Partition_2]
        else:
            Min_Right_2 = float("inf")
        
        #WE Know We Found The Median
        if(Max_Left_1 <= Min_Right_2 and Max_Left_2 <= Min_Right_1):
            if((m+n)%2):
                return max(Max_Left_1,Max_Left_2)
            else:
                return (max(Max_Left_1,Max_Left_2) + min(Min_Right_1,Min_Right_2)) / 2.0
        
        elif Max_Left_1 <= Min_Right_2:
            Min = Partition_1 + 1
        else:
            Max = Partition_1 - 1
        
Array1 = [1,3,5,7,9,11]
Array2 = [2,4,6,8,10,12]
Median = find_Median(Array1, Array2)
print("MEDIAN OF ARR 1 And ARR 2 is : " + str(Median))