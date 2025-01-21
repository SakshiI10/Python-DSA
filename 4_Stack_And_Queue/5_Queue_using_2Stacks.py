# Queue using two stacks

class QueueUsingStacks:
    def __init__(self):
        self.S1 = []  # Stack 1
        self.S2 = []  # Stack 2

    def EnQueue(self, data):
        self.S1.append(data)

    def DeQueue(self):
        # Check if S2 is empty
        if len(self.S2) == 0:
            # Transfer all elements from S1 to S2
            while len(self.S1) > 0:
                self.S2.append(self.S1.pop())

        # If S2 is still empty, the queue is empty
        if len(self.S2) == 0:
            print("DeQueue from an empty queue")
            return

        # Pop and return the top element from S2
        return self.S2.pop()


if __name__ == "__main__":
    Q = QueueUsingStacks()
    Q.EnQueue(1)
    Q.EnQueue(2)
    Q.EnQueue(3)
    print(Q.DeQueue())  # Output: 1
    print(Q.DeQueue())  # Output: 2
    Q.EnQueue(4)
    print(Q.DeQueue())  # Output: 3
    print(Q.DeQueue())  # Output: 4
    Q.DeQueue()         # Output: 4
