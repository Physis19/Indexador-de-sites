import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self._size = 0
    
    def add(self, data):
        if self.head == None:
            self.head = Node(data)
            self._size += 1
            return self.head.data
        else:
            new_node = Node(data)
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
            new_node.previous = current
            self._size += 1
            return new_node.data
        
    
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
        while current:
            if current.data == data and current == self.head:
                if not current.next:
                    self.head = None
                    return current.data
                
                else:
                    self.head = current.next
                    current.previous = None
                    return current.data
            
            elif current.data == data:
                if current.next:
                    nxt = current.next
                    prev = current.previous
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current.previous = None
                    return current.data
                
                else:
                    prev = current.previous
                    prev.next = None
                    current.previous = None
                    return current.data
            
            current = current.next

        raise ValueError(f'O site {data} não foi encontrado, verifique se a URL está correta')

    
    def show_list(self):
        current = self.head
        index = 0
        websites = []
        while current:
            website_data = (index, current.data)
            websites.append(website_data)
            current = current.next
            index += 1
        return websites

    def random_acess(self):
        current = self.head
        random_index = random.randint(0, self._size - 1)
        for i in range(random_index):
            current = current.next
        return current.data

    def __len__(self):
        return self._size

    def __repr__(self):
            r = ""
            current = self.head
            while(current):
                r = r + str(current.data) + "\n"
                current = current.next
            return r
        
    def __str__(self):
          return self.__repr__()

#lista = DoublyLinkedList()
#lista.add(1)
#lista.add(2)
#lista.add(3)
#print(lista)
#print('------------')
#removed = lista.remove(1)
#print(f'nó removido:{removed.data}')
#print('------------')
#print(lista)