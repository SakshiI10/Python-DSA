class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(head):
    if head is None:
        print("EMPTY LIST")
        return
    
    # Start from the head node
    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:  # Stop when we loop back to the head
            break
    print()

# Directly initialize the nodes
head = Node(1)  # First node (head)
second = Node(2)
third = Node(3)
fourth = Node(4)

# Connect the nodes to form a circular linked list
head.next = second
second.next = third
third.next = fourth
fourth.next = head
printList(head)
