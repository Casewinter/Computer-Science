# Main methods
# isEmpty ⇒ booleano;
# enqueue ⇒ add;
# peek ⇒ return value from next item;
# dequeue ⇒ return an item;
# size ⇒ size of queue;

class Queue:
    def __init__(self):
        self.queue =[]
        pass
    
    def isEmpty(self):
        if(len(self.queue) == 0):
            return True
        return False
    
    def enqueue(self, value):
        if(value == None):
            return
        self.queue.append(value)
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[0]
    
    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
