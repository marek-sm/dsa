class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def prepend(self, value):
        newHead = Node(value)
        newHead.next = self.head
        self.head = newHead
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)
    
    def delete(self, value):
        if self.head is None:
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next