import heapq

class PriorityQueue:

    def __init__(self):
        self.heap = []
        self.count = 0

    def enqueue(self, item, priority):
        """insert element to priority queue using priority."""
        heapq.heappush(self.heap, (priority, self.count,item))
        self.count+=1

    def dequeue(self):
        """return and remove element from the queue."""
        return heapq.heappop(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def peek(self):
        return self.heap[0]
    
    def size(self):
        return len(self.heap)

if __name__ == "__main__":
    pq = PriorityQueue()
    #Wakeup - 0, Brush - 1, BreakFast - 2, CatchBus - 3, Lunch - 4, Break - 5, Leave - 6
    pq.enqueue("Brush", 1) #FIFO
    pq.enqueue("Leave", 6)
    pq.enqueue("Wakeup", 0)
    pq.enqueue("BreakFast", 1)
    pq.enqueue("Break", 5)
    pq.enqueue("CatchBus", 3)
    pq.enqueue("Lunch", 4)

    print("Priority Queue:", pq.heap)

    print("Priority Queue -> Dequeue: ", pq.dequeue())
    print("Priority Queue -> Dequeue: ", pq.dequeue())
    print("Priority Queue -> Dequeue: ", pq.dequeue())
    print("Priority Queue -> Dequeue: ", pq.dequeue())
    print("Priority Queue -> Dequeue: ", pq.dequeue())
    print("Priority Queue -> Dequeue: ", pq.dequeue())


    

