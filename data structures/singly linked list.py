class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        pass

class linked_list:
    def __init__(self):
        self.head = None
        pass

    #O(1)
    def push(self, data):

        if(self.head == None):
            self.head = Node(data, None)
            return
        
        new_node = Node(data, self.head)
        self.head = new_node

    def delete_item(self, value):
        current = self.head
        prev = self.head
        
        if(current == None): 
            print("List is empty")
            return
        
        while(current != None):

            if(current.data == value):
                
                if(prev == self.head):
                    self.head = self.head.next
                prev.next = current.next
                print("Deleted")
                return
            
            prev = current
            current = current.next
 
        print("Not found")

    def pop(self):
        current = self.head
        prev = self.head
        
        if(current.next == None): 
            self.head = None
            print("List is empty")
            return
        
        while(current.next != None):
            prev = current
            current = current.next
        
        prev.next = None


    def printList(self):
        current = self.head

        if(current == None):
            print("List is empty")
            return
        
        while(current != None):
            print(current.data)
            current = current.next
