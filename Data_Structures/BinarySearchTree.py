# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:18:04 2018

@author: yahia
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data
        
#inserts value
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                    self.left.parent = self
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                    self.right.parent = self
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
#Returns true if found, else returns false
    def search_boolean(self,data):
        pointer = Node(self.data)        
        if self.data == data:
            return (True)
        
        elif self.data < data:
            if self.right is None:
                return (False)
            else:
                pointer = self.right
                return(pointer.search(data))
                
        elif self.data > data:
            if self.left is None:
                return (False)
            else:
                pointer = self.left
                return(pointer.search(data))
                
#Returns desired node, or node where we fell off tree
    def search(self,data):
        pointer = Node(self.data)        
        if self.data == data:
            return (self)
        
        elif self.data < data:
            if self.right is None:
                return (self)
            else:
                pointer = self.right
                return(pointer.search(data))
                
        elif self.data > data:
            if self.left is None:
                return (self)
            else:
                pointer = self.left
                return(pointer.search(data))
#finds node with minimum value
    def find_min (self):
        pointer = Node(self)
        if self.left is None:
            return (self)
        else:
            return(self.left.find_min())

    def find_max (self):
        pointer = Node(self)
        if self.right is None:
            return (self)
        else:
            return(self.right.find_max())
            

#Counts nodes    
    totalnumberofnodes = 0
    def count_nodes(self):
        global totalnumberofnodes
        totalnumberofnodes = 0
        self.count()
        return (totalnumberofnodes)
        
    def count(self):
        global totalnumberofnodes
        totalnumberofnodes+=1
        if self.left is not None:
            self.left.count()
        if self.right is not None:
            self.right.count()

#Finds Successor
    def successor(self):
        if self.right is not None:
            return(self.right.find_min())
        else:
            pointer = Node(self)
            while(pointer.data > pointer.parent.data):
                pointer = pointer.parent
            return(pointer.parent)
            
#Deletes a Node
    def Delete(self,Node):
        #Case 1: Node is a leaf
        if Node.left is None and Node.right is None:
            if Node.data > Node.parent.data:
                Node.parent.right = None 
                del(Node)
            elif Node.data < Node.parent.data:
                Node.parent.left = None
                del(Node)
        
        #Case 2: Node has one child
        elif Node.left is None and Node.right is not None:
            Node.parent.right = Node.right
            Node.right.parent = Node.parent
            del(Node)
            
        elif Node.right is None and Node.left is not None:
            Node.parent.left = Node.left
            Node.left.parent = Node.parent
            del(Node) 
        
        #Case 3: Node Has two children
        else:
            Successor = Node.successor()
            temp = Successor.data
            Successor.data = Node.data
            Node.data = temp
            Successor.Delete(Successor)
                
#Prints inorder Traversal    
    def PrintTree(self): #Inorder Traversal
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
            
#Creating Root of BST
root = Node(10)

#inserting values
root.insert(3)
root.insert(13)
root.insert(30)
root.insert(1)
root.insert(33)
root.insert(32)
root.insert(14)
root.insert(12)
root.insert(16)

#Searching
val = 3
if root.search(val):
    print("found it : " + str(val))
    
#Find Min
print("MIN VALUE IS : " + str(root.find_min().data))

    
#Find Max
print("Max VALUE IS : " + str(root.find_max().data))

#Find number of nodes
print("Total Number of Nodes : " + str(root.count_nodes()))

#Find Successor Examples
print("Successor of root is :" + str(root.successor().data))
print("Successor of 13 is :" + str(root.search(13).successor().data))

#Delete Examples
print("Deleting Root")
root.Delete(root)

root.PrintTree()
         
    