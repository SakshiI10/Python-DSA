# Array Implementation of Queue

class CircularQueue:
    def __init__(self, size):
        self.N = size
        self.front = -1
        self.rear = -1
        self.array = [None] * size

    def EnQueue(self, data):
        if (self.rear + 1) % self.N == self.front:
            print("Queue is full")
            return

        # If the queue is empty, set front to 0
        if self.front == -1:
            self.front = 0

        # Update rear index circularly and insert data
        self.rear = (self.rear + 1) % self.N
        self.array[self.rear] = data
        print(f"Enqueued: {data}")

    def DeQueue(self):
        if self.front == -1:
            print("Queue is empty")
            return -1

        # Get the data at the front
        data = self.array[self.front]

        # If there is only one element, reset front and rear
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            # Update front index circularly
            self.front = (self.front + 1) % self.N

        print(f"Dequeued: {data}")
        return data

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return

        print("Queue elements are:")
        i = self.front
        while True:
            print(self.array[i], end=" <-- ")
            if i == self.rear:
                break
            i = (i + 1) % self.N
        print()

if __name__ == "__main__":
    queue = CircularQueue(15)
    queue.display()
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.display()
    queue.DeQueue()
    queue.DeQueue()
    queue.display()