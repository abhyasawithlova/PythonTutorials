# Stack implementation.

# Is linear data structure, fallows LIFO principle.
# push() , pop(), peak(), isEmpty(), size() 
class MyStack:

    def __init__(self):
        self.stack = [] #list based stack.

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

    def pop(self) -> int:
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.stack.pop()

    def peek(self) -> None:
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.stack[-1]

    def display(self) -> None:
        #print elements in stack from last to first. 
        # [4, 
        #  3, 
        #  2, 
        #  1]
        if self.is_empty():
            print("Given stack is emtpy.")
            return

        print("[", end="")
        for i in range(self.size()-1, -1, -1):
            print(" " + str(self.stack[i]))
        print("]")



my_stack = MyStack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)

my_stack.display()

print(f"Size of the stack is: {my_stack.size()}")
item = my_stack.pop() # returns and remove top element from stack.
print(f"Item deleted from stack is: {item}")
print(f"Size of the stack is: {my_stack.size()}")

my_stack.display()

my_stack.push(5)

my_stack.display()

print(f"Peek element: {my_stack.peek()}")

