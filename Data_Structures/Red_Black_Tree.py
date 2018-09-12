
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data
        self.color = 'R'
        
class RB_Tree:
    def __init__(self,N):
        self.root = N
        self.root.color = 'B'
        
    def search(self,currnode, data):
        if currnode.data == data:
            return (True)
        elif currnode.data < data:
            if currnode.right is None:
                return (False)
            else:
                return(self.search(currnode.right,data))
        elif currnode.data > data:
            if currnode.left is None:
                return (False)
            else:
                return(self.search(currnode.left,data))
        
    def PrintTree(self,root): #Inorder Traversal
        currnode = root
        print(currnode.data)
        if(currnode.parent is not None):
            print("parent IS : " + str(currnode.parent.data),end="-->")
        if(currnode is not None):
            print("Color IS : " + str(currnode.color))
        if currnode.left:
            self.PrintTree(currnode.left)
        if currnode.right:
            self.PrintTree(currnode.right)
            
    def insert(self,data):
        currnode = self.root
        newnode = Node(data)
        self.insert_Recursive(currnode,newnode,data)
        if(newnode.parent is None):
            newnode.color = 'B'
            return
        self.fix_Violations(newnode)

    
    def insert_Recursive(self,currnode, newnode,data):
        if currnode.data:
            if data < currnode.data:
                if currnode.left is None:
                    newnode.parent= currnode
                    currnode.left = newnode
                else:
                    self.insert_Recursive(currnode.left,newnode,data)
            else:
                if currnode.right is None:
                    newnode.parent = currnode
                    currnode.right = newnode
                else:
                    self.insert_Recursive(currnode.right,newnode,data)
    
    def fix_Violations(self,Pointer):
        N = Pointer
        if(self.root == N):
            N.color = 'B'
            return
        
        while(N.parent is not None and N.parent.color == 'R'):
            if(N.parent.parent.left == N.parent):
                if(N.parent.parent.right is not None):
                    if(N.parent.parent.right.color == 'R'):
                        N.parent.color = 'B'
                        N.parent.parent.right.color = 'B'
                        N.parent.parent.color = 'R'
                        N = N.parent.parent
                else:
                    if(N.parent.right == N):
                        N = N.parent
                        self.leftRotate(N,N.right)
                    N.parent.color = 'B'
                    N.parent.parent.color = 'R'
                    self.rightRotate(N.parent.parent,N.parent.parent.left)
            else:
                if(N.parent.parent.left is not None):
                    if(N.parent.parent.left.color == 'R'):
                        N.parent.color = 'B'
                        N.parent.parent.left.color = 'B'
                        N.parent.parent.color = 'R'
                        N = N.parent.parent
                else:
                    if(N.parent.left == N):
                        N = N.parent
                        self.rightRotate(N,N.left)
                    N.parent.color = 'B'
                    N.parent.parent.color = 'R'
                    self.leftRotate(N.parent.parent,N.parent.parent.right)
            self.root.color = 'B'
            
                
    
    def leftRotate(self, G,P) :
        if P is None:
            return
        else:
            if P.left is not None:
                G.right = P.left
                P.left.parent = G
            else:
                G.right = None
        if G.parent is not None:
            P.parent = G.parent
        if G.parent is None:
            self.root = P
            self.root.parent = None
        else:
            if G == G.parent.left:
                G.parent.left = P
            else:
                G.parent.right = P
        P.left = G
        G.parent = P
        
    
    def rightRotate(self, G,P) :
        if P is None:
            return
        else:
            if P.right is not None:
                G.left = P.right
                P.right.parent = G
            else:
                G.left = None
        if G.parent is not None:
            P.parent = G.parent
        if G.parent is None:
            self.root = P
            self.root.parent = None
        else:
            if G == G.parent.left:
                G.parent.left = P
            else:
                G.parent.right = P
        P.right = G
        G.parent = P
            
            
        
       
        
root = Node(10)
RB = RB_Tree(root)
RB.insert(11)
RB.insert(12)
RB.insert(13)
RB.insert(14)
RB.insert(15)
RB.insert(1)
RB.insert(3)
RB.insert(4)
RB.insert(5)


RB.PrintTree(RB.root)
if(RB.search(RB.root,10)):
    print("FOUND ")
        
        
    
        