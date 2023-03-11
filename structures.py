class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            self._size += 1
        else:
            new_node = Node(data)
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
            new_node.previous = current
            self._size += 1
    
    def prepend(self,data):
        if self.head == None:
            self.head = Node(data)
            self._size += 1
        else:
            new_node = Node(data)
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            self._size += 1
    
    def remove(self, data: str):
        current = self.head
        while (current):
            if current.data == data and current == self.head:
                if current.next == None:
                    current = None
                    self.head = None
                    self._size -= 1
                    return
        
                else:
                    temp = current.next
                    current.next = None
                    temp.previous = None
                    current = None
                    self.head = temp
                    self._size -= 1
                    return
            
            elif current.data == data:
                if current.next:
                    nxt = current.next
                    previous = current.previous
                    previous.next = nxt
                    nxt.previous = previous
                    current.next = None
                    current.previuous = None
                    current = None
                    self._size -= 1
                    return
                else:
                    previous = current.previous
                    previous.next = None
                    current.previous = None
                    current = None 
                    self._size -= 1
                    return
        current = current.next

          
    def __repr__(self):
            r = ""
            current = self.head
            while(current):
                r = r + str(current.data) + "\n"
                current = current.next
            return r
        
    def __str__(self):
          return self.__repr__()
