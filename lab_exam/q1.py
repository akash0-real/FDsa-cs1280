class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return
       if self.head.next is None:
             self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <> ")
            current = current.next
        print("None")
        
dll = DoublyLinkedList()
dll.insert_at_beginning(30)
dll.insert_at_beginning(20)
dll.insert_at_beginning(10)

print("List after insertions:")
dll.display()

dll.delete_first()
print("List after deleting first node:")
dll.display()
