class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

head = Node(10)
second = Node(20)
third = Node(30)

# Linking the nodes
head.next = second
second.prev = head
second.next = third
third.prev = second

# Function to print the doubly linked list
def printDoublyLinkedList(head):
    temp = head
    while temp:
        print(temp.data, end=" <=> ")
        temp = temp.next
    print("None")  # Indicates the end of the doubly linked list

# Print the doubly linked list
printDoublyLinkedList(head)
