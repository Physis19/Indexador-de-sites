class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self._size = 0
    
    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer: 
                pointer = pointer.next
            else:
                raise IndexError
        return pointer 
    
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
    
    def add_node_after(self, index, data):
        current = self.head
        while (current):
            if current.next == None and current.data == index:
                self.append(data)
            
          
    def __repr__(self):
            r = ""
            pointer = self.head
            while(pointer):
                r = r + str(pointer.data) + "\n"
                pointer = pointer.next
            return r
        
    def __str__(self):
          return self.__repr__()



