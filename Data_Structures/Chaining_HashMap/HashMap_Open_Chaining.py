# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:18:04 2018

@author: yahia
"""
from LinkedList import Ordered_Linked_List
from Node import Node
        
        
class HashMap_Open_Chaining(object):
    def __init__(self,slots = 13):
        self.array = []
        self.numberofelements = 0
        for x in range(slots):
            x = Ordered_Linked_List(float("-infinity"))
            self.array.append(x)
        self.length = slots
        
    def Hash_Function(self,number):
        return (number % self.length)
    
    def insert(self,number):
        self.numberofelements+=1
        key = self.Hash_Function(number)
        self.array[key].Insert(number)
        
    def search(self,number):
        key = self.Hash_Function(number)
        node = self.array[key].Search(number)
        if node is not None:
            return True
        return False
    
    def delete(self,number):
        self.numberofelements -= 1
        key = self.Hash_Function(number)
        self.array[key].Delete(number)
        
    def printHashMap(self):
        for index in range(self.length):
            print("Slot #" + str(index) + " : ", end="")
            self.array[index].printNodes()
    
    
myhashmap = HashMap_Open_Chaining()
myhashmap.insert(2243)
myhashmap.insert(2343)
myhashmap.insert(20)
myhashmap.insert(9)
myhashmap.insert(8)
myhashmap.insert(654)
myhashmap.insert(123)
myhashmap.insert(5)

myhashmap.printHashMap()

myhashmap.search(123)
myhashmap.search(100)
myhashmap.delete(123)
myhashmap.search(123)





            
            