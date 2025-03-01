# Create a Linked List with Primary numbers and sum the values.
from math import sqrt

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """
        Add node to end of the LinkedList.
        """
        # is data a numeric value.
        value = int(data)

        # is data a primary number.
        if value < 2:
            print(f"{data} is not a prime hence ignoring.")
            return
        
        sq_rt = sqrt(value)
        print(f"{sq_rt} is sqrt({data})")

        for i in range(2, int(sq_rt) + 1):
            if value % i == 0:
                print(f"{data} is not a prime hence ignoring.")
                return

        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            if cur_node == self.tail:
                break  # Stop traversal if we reach the tail node
            cur_node = cur_node.next
        print("None")

    def sum(self):
        curr = self.head
        if curr is None:
            print("Linked List is empty, hence sum of all nodes is 0")
            return

        if curr == self.tail: # single node linked list.
            print(f"sum of all nodes is {curr.data}")
            return

        tot = 0 #21
        while curr:
            tot = tot + curr.data
            #if curr == self.tail:
            #    return
            curr = curr.next
        print(f"Sum of all nodes is {tot}")


ll = LinkedList()
#ll.append(1)
ll.append(2)
#ll.append(3)
#ll.append(5)
#ll.append(8)
#ll.append(11)
#ll.append("a") # is it numeric?
ll.print_list()
ll.sum()

