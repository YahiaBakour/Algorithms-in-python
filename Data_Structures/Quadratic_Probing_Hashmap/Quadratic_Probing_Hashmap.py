# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:18:04 2018

@author: yahia
"""
    
from Node import Node
    
class Hash_map_Quadratic_Probing(object):
    def __init__(self,slots = 13):
        self.array = [Node(None)] * slots
        self.numberofelements = 0
        self.length = slots
        
    def Hash_Function(self,number,i):
        return ((number + 3 + 5*i + 7*(i**2)) % self.length)
    
    def insert(self,number):
        self.numberofelements+=1
        i = 0
        key = self.Hash_Function(number,i)
        NewNumb = Node(number)
        NewNumb.key = key
        while(self.array[key].data is not None and not self.array[key].dead):
            if(self.array[key].key != NewNumb.key):
                raise NameError('Table is Full')
            i+=1
            key = self.Hash_Function(number,i)
        self.array[key] = NewNumb
        
    def Delete(self,Number):
        i = 0
        key = self.Hash_Function(Number,i)
        nodeatkey = self.array[key]
        while(nodeatkey.data != Number and i != self.length):
            i+=1
            key = self.Hash_Function(Number,i)
            nodeatkey = self.array[key]
        if i == self.length:
                raise NameError('Value isnt in table')
        if(self.array[key].dead):
                raise NameError('Value is already dead')

        self.array[key].dead = True

        
    def printHashMap(self):
        for index in range(self.length):
            print("Slot #" + str(index) + " : ", end="")
            print(self.array[index].data)
    
    
myhashmap = Hash_map_Quadratic_Probing()
myhashmap.insert(2243)
myhashmap.insert(2343)
myhashmap.insert(2343)
myhashmap.insert(2343)





myhashmap.printHashMap()





            
            