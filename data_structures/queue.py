class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
    
    def dequeue(self):
        if self.head is None:
            self.tail = None
            return
        removed_value = self.head.data
        self.head = self.head.next
        return removed_value
    
    def peek_front(self):
        if self.head is None:
            return None
        return self.head.data

    def is_empty(self):
        return not self.head