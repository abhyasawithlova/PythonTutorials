class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    Demonestrates basic operations of LinkedList.
    1. append node, 
    2. prepend node, 
    3. insert node Y after node X, 
    4. delete, 
    5. delete at position, 
    6. search for key, 
    7. print nodes,
    8. delete duplicate nodes ( sorted and unsorted )
    9. reverse
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """
        Add node to end of the LinkedList.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        """
        Add node to start of the LinkedList.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        if prev_node == self.tail:
            self.tail = new_node

    def delete_node(self, key):
        """
        Find the node with key as data, and delete.
        """
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            if cur_node == self.tail:
                self.tail = None
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        if cur_node == self.tail:
            self.tail = prev
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            if cur_node == self.tail:
                self.tail = None
            cur_node = None
            return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev.next = cur_node.next
        if cur_node == self.tail:
            self.tail = prev
        cur_node = None

    def search(self, key):
        cur_node = self.head
        while cur_node:
            if cur_node.data == key:
                return True
            cur_node = cur_node.next
        return False

    def remove_duplicates_unsorted(self):
            if self.head is None:
                return

            current = self.head
            seen = set([current.data])
            while current.next:
                if current.next.data in seen:
                    current.next = current.next.next
                else:
                    seen.add(current.next.data)
                    current = current.next
            self.tail = current  # Update the tail node

    def remove_duplicates_sorted(self):
        if self.head is None:
            return

        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        self.tail = current  # Update the tail node

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev # reversing nodes
            prev = current
            current = next_node
        self.tail = self.head
        self.head = prev
        

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            if cur_node == self.tail:
                break  # Stop traversal if we reach the tail node
            cur_node = cur_node.next
        print("None")


# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
ll.insert_after_node(ll.head.next, 1.5)
ll.print_list()  # Output: 0 -> 1 -> 1.5 -> 2 -> 3 -> None
ll.delete_node(1.5)
ll.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None
print(ll.search(2))  # Output: True
print(ll.search(4))  # Output: False

ll.reverse()
ll.print_list()
#Testing duplicate removal from LinkedList
ll2 = LinkedList()
ll2.append(1)
ll2.append(2)
ll2.append(2)
ll2.append(3)  
ll2.remove_duplicates_sorted()
ll2.print_list()

ll3 = LinkedList()
ll3.append(1)
ll3.append(2)
ll3.append(3)
ll3.append(4)
ll3.append(3)
ll3.append(2)  
ll3.remove_duplicates_unsorted()
ll3.print_list()

# Create a linked List of Primary Number and Print sum of LinkedList.