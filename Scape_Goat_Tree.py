import numpy as np
import math

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data

        
class SGTree:
    def __init__(self,N):
        self.root = N
        self.size = 1
        
    def Search(self,data):
        Pointer = self.root
        
        while(Pointer is not None):
            if(data == Pointer.data):
                return True
            elif (data > Pointer.data) :
                Pointer = Pointer.right
            else:
                Pointer = Pointer.left
                    
        return False
    
            
    def log32(self,n):
        log23 = 2.4663034623764317
        return (math.ceil(log23 * np.log(n)))
    
    def count(self,N):
        if(N is None):
            return 0
        return (1 + self.count(N.left) + self.count(N.right))
    
    def PrintTree(self,root): #Inorder Traversal
        currnode = root
        print(currnode.data, end = " : ")
        if(currnode.right is not None):
            print("Right IS : " + str(currnode.right.data),end = " -- ")
        if(currnode.left is not None):
            print("Left IS : " + str(currnode.left.data),end = " -- ")
        if(currnode.parent is not None):
            print("Parent IS : " + str(currnode.parent.data),end = " -- ")
        print()
        if currnode.left:
            self.PrintTree(currnode.left)
        if currnode.right:
            self.PrintTree(currnode.right)
            
    def insert(self,currnode,data):
        newnode = Node(data)
        self.size += 1
        depth = self.insert_Recursive_and_return_depth(currnode,newnode,data)
        if depth > self.log32(self.size):
            P = newnode.parent
            while(3 * self.count(P) <= 2 * self.count(P.parent)):
                P = P.parent
            self.rebuild_Tree(P.parent,P.parent.parent)
        
    def rebuild_Tree(self,U,P):
        n = self.count(U)
        newnode = Node(None)
        Array = [newnode] * self.size
        self.storeinarray(U,Array,0)
        if P is None:
            self.root = self.buildBalancedFromArray(Array,0,n)
        elif P.right == U:
            P.right = self.buildBalancedFromArray(Array,0,n)
            P.right.parent = P
        else:
            P.left = self.buildBalancedFromArray(Array,0,n)
            P.left.parent = P
            
    def storeinarray(self,N,array,i):
        if N is None or N.data is None:
            return i
        i = self.storeinarray(N.left,array,i)
        i+=1
        array[i] = N
        return self.storeinarray(N.right,array,i)
    
    
    def buildBalancedFromArray(self,a,i,n):
        if n == 0:
            return None
        m = n //2
        a[i+m].left = self.buildBalancedFromArray(a,i,m)
        if(a[i+m].left is not None):
            a[i+m].left.parent = a[i+m]
        a[i+m].right = self.buildBalancedFromArray(a,i+m+1,n-m-1)
        if(a[i+m].right is not None):
            a[i+m].right.parent = a[i+m]            
        return(a[i+m])
        
    def insert_Recursive_and_return_depth(self,currnode, newnode,data):
        if currnode.data:
            if(currnode is None):
                return 0
            if data < currnode.data:
                if currnode.left is None:
                    newnode.parent= currnode
                    currnode.left = newnode
                    return 0
                else:
                    return (1 + self.insert_Recursive_and_return_depth(currnode.left,newnode,data))
            else:
                if currnode.right is None:
                    newnode.parent = currnode
                    currnode.right = newnode
                    return 0
                else:
                    return (1 + self.insert_Recursive_and_return_depth(currnode.right,newnode,data))
   
            
        
       
        
root = Node(10)
SGTree = SGTree(root)
SGTree.insert(root,11)
SGTree.insert(root,12)
SGTree.insert(root,13)
SGTree.insert(root,14)
SGTree.insert(root,15)
SGTree.insert(root,16)
SGTree.insert(root,18)
SGTree.insert(root,19)
SGTree.insert(root,20)
SGTree.insert(root,21)
SGTree.insert(root,22)
SGTree.insert(root,23)

SGTree.PrintTree(SGTree.root)

if(SGTree.Search(23)):
    print("Found")

        
        
    
        