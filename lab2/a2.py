class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None 
    def append_node(self, data):
        new_node = Node(data)  
        if not self.head:
            self.head = new_node  
            return
        current = self.head
        while current.next:
            current = current.next  
        current.next = new_node  

    def search_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True 
            current = current.next
        return False 

    def display_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  


if __name__ == "__main__":
    ll = LinkedList()
    ll.append_node(10) 
    ll.append_node(20)
    ll.append_node(30)
    ll.display_list() 
    print(ll.search_node(20))  
    print(ll.search_node(40))
