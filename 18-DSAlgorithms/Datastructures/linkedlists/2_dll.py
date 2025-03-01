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
        self.size = 0

    def append(self, data):
        """
        Append node at tail.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size+=1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.size+=1

    def prepend(self, data):
        """
        Append node at front.
        """
        new_node = Node(data)
        curr = self.head
        new_node.next = curr
        curr.prev = new_node
        self.head = new_node
        self.size+=1


    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            if curr == self.tail:
                break
            curr = curr.next
        print("None")

    def reverse(self):
        curr = self.head
        
        if curr is None:
            print("No nodes exist.")
            return
        
        if curr == self.tail:
            print("Linked List having single node, hence reverse is also same.")
            return
        
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        
        self.head, self.tail = self.tail, self.head

    def delete_node(self, k) -> None:
        curr = self.head
        if curr is None:
            print(f"Linked list is empty, hence {k} cannot be deleted.")
            return
        
        if curr.data == k:
            self.head = curr.next
            self.size-=1
            print(f"Delete: Found {k} at head, hence deleting head, new size is {self.size}")
            return
        
        if self.tail.data == k:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size-=1
            print(f"Delete: Found {k} at tail, hence deleted tail, new size is {self.size}")
            return
        
        curr = curr.next # start lookup from 2nd node.
        ni=1
        while curr:
            prev_node = None
            next_node = None
            if curr.data == k:
                prev_node = curr.prev
                next_node = curr.next
                prev_node.next = curr.next
                next_node.prev = prev_node
                self.size-=1
                print(f"Delete: {k} found at position {ni}, and deleted, and new size is {self.size}")
                break
            ni+=1
            curr = curr.next

    def search(self, k) -> None:
        curr = self.head
        if curr is None:
            print(f"Search: Linked list is empty, hence {k} cannot be found.")
            return
        
        if curr.data == k:
            print(f"Search: {k} found at head node at 0 position")
            return
        
        if self.tail.data == k:
            print(f"Search: {k} found at tail node, at position {self.size - 1}") # how to print node position?
            return
    
        ni = 1
        curr = curr.next # moving to next data, as we have already verified in current node.
        while curr:
            if curr.data == k:
                print(f"Search: {k} found at Node, position {ni}")
                return
            ni+=1
            curr = curr.next
        
        print(f"Search: {k} not found in Linked List.")

    def cal_size(self) -> int:
        curr = self.head
        ni=0
        while curr:
            ni+=1
            curr = curr.next
        return ni


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
dll.reverse()
dll.print_list()
dll.search(3)
dll.delete_node(2)
dll.print_list()
dll.delete_node(1)
dll.print_list()
