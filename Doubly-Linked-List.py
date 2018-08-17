# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:18:04 2018

@author: yahia
"""

class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        
class Ordered_Linked_List:
    def __init__(self):
        self.root = None
        self.tail = None
        
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
                print("found")
                return pointer
            else:
                print("not found")
                return None
            
    def Delete(self,data): #to insert data into the Linked List
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
            print("Root and only element is : " + str(self.root.data))
        else:
            pointer = self.root
            while(pointer is not None):
                if pointer.right is not None:
                    print(str(pointer.data) + " --> ",end = "")
                else:
                    print(str(pointer.data))
                pointer = pointer.right
        
myDLL = Ordered_Linked_List(1)      

myDLL.Insert(2)
myDLL.Insert(25)
myDLL.Insert(22)
myDLL.Insert(1112)
myDLL.Insert(222)

myDLL.printNodes()  
print ("Max is : " + str(myDLL.Find_Max().data))
print ("Min is : " + str(myDLL.Find_Min().data))   

print("Searching for 222: ",end="")
myDLL.Search(222)
print("deleting 222")
myDLL.Delete(222)
print("Searching for 222: ",end="")
myDLL.Search(222)


            
            