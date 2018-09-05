# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:18:04 2018

@author: yahia
"""
from LinkedList import Ordered_Linked_List
from Node import Node

class Ordered_Linked_List(object):
    def __init__(self,data):
        self.Tail = None
        self.root = Node(data)
        

    def Insert(self,data): #to insert data into the Linked List
        newNode = Node(data)
        #case 1: No root
        if self.root == None:
            self.root = newNode
            self.tail = None
            return
        #case2: Insert to head
        elif self.root.data > data:
            newNode.right = self.root
            self.root.left = newNode
            self.root = newNode
            self.tail = newNode.right
            return
        
        #case3: Insert to tail or middle
        else: 
            pointer = self.root
            while(pointer.right is not None and pointer.right.data <= data):
                pointer = pointer.right
            
            if(pointer.right is None):
                pointer.right = newNode
                newNode.left = pointer
                self.tail = newNode 
                return
            else:
                newNode.left = pointer
                newNode.right = pointer.right
                pointer.right = newNode
                newNode.right.left = newNode
                return
            
    def Search(self,data): #to insert data into the Linked List
    #case 1: No root
        if self.root == None:
            print("Not Found, LL Empty")
            return None
        #case3: Insert to tail or middle
        else: 
            pointer = self.root
            while(pointer.right is not None and pointer.right.data <= data):
                pointer = pointer.right
            
            if(pointer.data == data):
                print("found : "+ str(data))
                return pointer
            else:
                print("not found : " + str(data))
                return None
            
    def Delete(self,data): #to insert data into the Linked List
        print("Deleting " + str(data) + " ....")
    #case 1: No root
        if self.root == None:
            print("Cannot Delete, LL Empty")
            return None
    #Case2 : Delete from head
        elif self.root.data == data:
            self.root.right.left = None
            self.root = self.root.right
            return None
    #case 3 : Delete from tail
        elif self.tail.data == data:
            self.tail.left.right = None
            self.tail = self.tail.left
    #case 4: Delete from middle
        else: 
            pointer = self.root
            while(pointer.right is not None and pointer.right.data <= data):
                pointer = pointer.right
            if(pointer.data == data):
                pointer.left.right = pointer.right
                pointer.right.left = pointer.left
                return None
            else:
                print("Cannot Be deleted, it doesnt exist")
                return None
            
    def Find_Max(self):
        return self.tail
    
    def Find_Min(self):
        return self.root
            
    def printNodes(self):
        if self.root is None:
            print("Empty DLL")
        elif self.root.right is None:
            print(str(self.root.data))
        else:
            pointer = self.root
            while(pointer is not None):
                if pointer.right is not None:
                    print(str(pointer.data) + " --> ",end = "")
                else:
                    print(str(pointer.data))
                pointer = pointer.right
        
        
        
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





            
            