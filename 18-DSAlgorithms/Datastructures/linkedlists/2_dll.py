class Node:
    def __init__(self, data):
        self.prev=None
        self.data = data
        self.next = None

class DLinkedList:
    """
    Demonestrates basic operations of Doubly LinkedList.
    1. append node, 
    2. prepend node, 
    3. add node Y after X, 
    4. delete node, 
    5. delete node Y after X, 
    6. search, 
    7. print nodes
    8. reverse
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        curr = self.head
        new_node.next = curr
        curr.prev = new_node
        self.head = new_node


    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            if curr == self.tail:
                break
            curr = curr.next
        print("None")

# Example usage

dll = DLinkedList()
dll.append(1)
dll.print_list()
dll.append(2)
dll.print_list()
dll.append(3)
dll.append(4)
dll.print_list()
dll.prepend(0)
dll.print_list()
