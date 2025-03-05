# Linked List implementation of Stack

class Node:
    def __init__(self, data):
        self.data = data             # The value stored in the node
        self.next = None             # Pointer to the next node

class Stack:
    def __init__(self):
        self.top = None              # The top node of the stack

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)       # Create a new node
        new_node.next = self.top     # Point the new node to the current top
        self.top = new_node          # Update the top to the new node
        print(value, "pushed onto the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
            return None
        popped_value = self.top.data # Retrieve the data from the top node
        self.top = self.top.next     # Move the top pointer to the next node
        print(popped_value, "popped from the stack.")
        return popped_value

    def peek(self):
        if self.is_empty():
            print("Stack is Empty. No top element.")
            return None
        return self.top.data

if __name__ == "__main__":
    stack = Stack()                  # Create an empty stack
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    print("Top element:", stack.peek())  # View the top element
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()                      # Attempt to pop from an empty stack
    print("Is stack empty?", stack.is_empty())  # Check if the stack is empty
