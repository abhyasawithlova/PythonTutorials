# Queue implementation using Arrays.


class MyQueue:

    def __init__(self, size=10):
        self.queue = []
        self.max_size = size

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Queue is Overflow")
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the first item from the queue."""
        if not self.is_empty():
            return self.queue.pop(0) #always top element should be returned, because queue fallow FIFO rule.
        raise IndexError("Queue is Underflow")

    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        """Check if the queue is full."""
        return len(self.queue) >= self.max_size

    def peek(self):
        """Return the first item from the queue without removing it."""
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("Peek from empty queue")

    def size(self):
        return len(self.queue)

    def print(self):
        """Print the current state of the queue."""
        print("Current Queue:", self.queue)

if __name__ == "__main__":
    my_queue = MyQueue(size=5)
    my_queue.enqueue(1)
    my_queue.print()

    # I am going to insert 5 more elements.
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    my_queue.enqueue(5)
    #my_queue.enqueue(6)  # This will raise an exception if the queue is full
    my_queue.print()

    print("Dequeue Element: ", my_queue.dequeue())  # Dequeue an item
    my_queue.print()
    print("Dequeue Element: ", my_queue.dequeue())  # Dequeue another item
    my_queue.print()

    my_queue.enqueue(6)  # Enqueue another item
    my_queue.print()
    print("Queue size after inserting items:", my_queue.size())

