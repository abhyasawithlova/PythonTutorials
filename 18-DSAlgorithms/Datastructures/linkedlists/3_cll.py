#Circular Linked List
## Last node of the linked list having reference to first hence forms a circular linked list.

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        """
        Append node at tail.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            if curr == self.tail:
                break
            curr = curr.next
        print("None")

cll = CircularLinkedList()
cll.append(0)
cll.append(1)

cll.print_list()
    