
class MyQueue:

    def __init__(self):
        self.queue = [] #python array.

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the first item from the queue."""
        if not self.is_empty():
            return self.queue.pop(0) #always top element should be returned, because queue fallow FIFO rule.
        raise IndexError("Queue is Underflow")

    def is_empty(self):
        return len(self.queue) == 0
    
    def peek(self):
        """Return the first item from the queue without removing it."""
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("Peek from empty queue")

    def size(self):
        return len(self.queue)
    
    def is_full(self, max_size):
        """Check if the queue is full."""
        return len(self.queue) >= max_size


if __name__ == "__main__":
    my_queue = MyQueue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    print("Queue size after inserting items:", my_queue.size())
    print("First item in queue:", my_queue.peek())
    print("Size of the queue after peek:", my_queue.size())

    print("Dequeue item:", my_queue.dequeue())
    print("Queue size after dequeue:", my_queue.size())
    my_queue.dequeue()  # Dequeue another item
    my_queue.dequeue()  # Dequeue another item
    my_queue.dequeue()  # Dequeue another item
