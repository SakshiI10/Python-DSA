# Array implementation of Stack

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity  # Preallocate memory for the stack
        self.top = -1                   # Initialize the top pointer

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.is_full():
            print("Stack is full")
            return
        self.top += 1
        self.array[self.top] = value
        print(value, "pushed onto the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
            return None                 # Return None to indicate the stack is empty
        data = self.array[self.top]
        self.top -= 1
        print(data, "popped from the stack.")
        return data

    def peek(self):
        if self.is_empty():
            print("Stack is Empty. No top element.")
            return None
        return self.array[self.top]

if __name__ == "__main__":
    stack = Stack(3)                    # Create a stack with a capacity of 5
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    print("Top element:", stack.peek()) # View the top element
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()                         # Attempt to pop from an empty stack
    print("Is stack empty?", stack.is_empty())  

# Limitation of Array based Implementation: The maximum size of the stack must first be defined and it cannot be changed.