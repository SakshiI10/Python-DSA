# Stack using two queues

from queue import Queue

class StackUsingQueues:
    def __init__(self):
        self.Q1 = Queue()  # First queue
        self.Q2 = Queue()  # Second queue

    def push(self, data):
        # Push element in empty stack
        if len(self.Q1.queue) != 0:  # Check if Q1 is not empty
            self.Q1.put(data)
        else:
            self.Q2.put(data)

    def pop(self):
        if len(self.Q1.queue) == 0 and len(self.Q2.queue) == 0:  # Check if both queues are empty
            print("Pop from an empty stack")
            return None

        # If Q1 is not empty, transfer elements to Q2
        if len(self.Q1.queue) != 0:
            while len(self.Q1.queue) > 1:
                self.Q2.put(self.Q1.get())
            return self.Q1.get()

        # If Q2 is not empty, transfer elements to Q1
        while len(self.Q2.queue) > 1:
            self.Q1.put(self.Q2.get())
        return self.Q2.get()
  
if __name__ == "__main__":
    stack = StackUsingQueues()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())  # Output: 3
    print(stack.pop())  # Output: 2
    stack.push(4)
    print(stack.pop())  # Output: 4
    print(stack.pop())  # Output: 1
    stack.pop()         # Output: Pop from an empty stack