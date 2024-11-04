class SinglyNode:
    def __init__(self, data: any=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: any):
        new_node = SinglyNode(data)

        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node
    
    def display(self):
        current = self.head
        
        while current:
            print(current.data, end=" -> ")
            current = current.next
        
        print("None")

l1 = SinglyLinkedList()

l1.append(1)
l1.append(2)
l1.append(3)

l1.display()


class DoublyNode:
    def __init__(self, data: any=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = DoublyNode(data)

        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node
        new_node.prev = last
    
    def display(self):
        current = self.head

        while current:
            print(current.data, end=" <-> ")
            current = current.next
        
        print("None")

l2 = DoublyLinkedList()

l2.append(10)
l2.append(20)
l2.append(30)

l2.display()


class CurcularLinkedList():
    def __init__(self):
        self.head = None

    def append(self, data:any):
        new_node = SinglyNode(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        last = self.head
        while last.next != self.head:
            last = last.next
        
        last.next = new_node
        new_node.next = self.head
    
    def display(self):
        current = self.head
        
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        
        print(f"Head ({self.head.data})")

l3 = CurcularLinkedList()

l3.append(100)
l3.append(200)
l3.append(300)

l3.display()