from queue import Queue

def main():
    q = Queue(maxsize=5)
    
    # insert an element to queue.
    q.put(1)
    print("Inserted 1 to queue ")
    q.put(2)
    print("Inserted 2 to queue ")
    q.put(3)
    print("Inserted 3 to queue ")
    q.put(4)
    print("Inserted 4 to queue ")
    print(q)

    for _ in range(q.qsize()):
        print(q.get(), end=' ')

    print(q.empty())  # Check if the queue is empty

    #print(q.get(block=True, timeout=2))  # This will block until an item is available or timeout occurs

    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    q.put(5)
    print(f"Is My Queue full: {q.full()}")  # Check if the queue is full
    q.put(6, block=False)  # This will raise an exception if the queue is full
    q.put_nowait(6)
    

if __name__ == "__main__":
    main()





