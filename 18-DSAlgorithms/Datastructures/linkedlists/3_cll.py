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
            self.tail.next = self.head # making head as next.
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head # making head as next.


    def is_circular_ll(self):
        curr = self.head
        while curr:
            if curr.next == self.head:
                print("Yes given linked list is forming circle.")
                break
            curr = curr.next
        if curr is None:
            print("No, given linked list is not forming a circle.")

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            if curr.next == self.head:
                break
            curr = curr.next
        print("None")

cll = CircularLinkedList()
cll.append(0)
cll.append(1)
cll.append(2)
cll.append(3)

cll.print_list()
cll.is_circular_ll()
# breacking circle, tail.next should be None.
cll.tail.next = None
cll.is_circular_ll()
    