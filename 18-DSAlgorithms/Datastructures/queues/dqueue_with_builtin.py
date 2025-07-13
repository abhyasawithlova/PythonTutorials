from collections import deque


if __name__ == "__main__":
    my_dqueue = deque(maxlen=5)  # Create a deque with a maximum length of 5
    my_dqueue.append(1)
    print(my_dqueue)
    my_dqueue.append(2)
    my_dqueue.append(3)
    my_dqueue.append(4)
    my_dqueue.append(5)
    print("Deque after adding 5 elements:", my_dqueue)
    my_dqueue.append(6)  # This will remove the oldest element (1)
    print("Deque after adding 6th element (oldest removed):", my_dqueue)

    my_dqueue.extend([7, 8, 9])  # Extend the deque with multiple elements
    print("Deque after extending with 3 more elements:", my_dqueue)

    my_dqueue.popleft()  # Remove the oldest element (2)
    print("Deque after popping the leftmost element:", my_dqueue)
    my_dqueue.pop()  # Remove the newest element (9)
    print("Deque after popping the rightmost element:", my_dqueue)