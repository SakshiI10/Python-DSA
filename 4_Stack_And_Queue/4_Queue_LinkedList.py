class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, new_data):
        new_node = Node(new_data)

        # If the queue is empty, the new node is both the front and rear
        if self.rear is None:
            self.front = self.rear = new_node
            print(f"Enqueued: {new_data}")
            return

        # Add the new node at the end of the queue and update rear
        self.rear.next = new_node
        self.rear = new_node
        print(f"Enqueued: {new_data}")

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return

        # Move the front to the next node
        temp = self.front
        self.front = self.front.next

        # If front becomes None, update rear to None
        if self.front is None:
            self.rear = None

        print(f"Dequeued: {temp.data}")
        return temp.data  # Optionally return the dequeued data

if __name__ == "__main__":
    q = Queue()

    # Enqueue elements into the queue
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    # Dequeue elements from the queue
    q.dequeue()
    q.dequeue() 