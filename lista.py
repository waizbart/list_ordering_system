from node import Node

class ListaSE:
    def __init__(self):
        self.head = None  # Cabeça da lista
        self.size = 0

    def insert(self, data):
        #Insere um nó no início da lista.
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def remove(self, data):
       #Remove um nó da lista pelo valor
        current = self.head
        prev = None
        while current is not None:
            if current.value == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.size -= 1
                return True  # Dado encontrado e removido
            prev = current
            current = current.next
        return False  # Dado não encontrado

    def display(self):
        #Exibe os elementos da lista.
        print("[ ", end="")
        current = self.head
        while current:
            print(current.value, end="")
            current = current.next
            if current:
                print(", ", end="")
        print(" ]")
        
    def at(self, index):
        #Retorna o dado de um nó em uma posição específica
        if index >= self.size:
            raise IndexError("Índice fora do alcance")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value
    
    def change(self, index, data):
        #Muda o valor de um nó em uma posição específica
        if index >= self.size:
            raise IndexError("Índice fora do alcance")
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = data

    def __len__(self):
        return self.size


