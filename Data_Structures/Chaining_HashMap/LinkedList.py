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
        