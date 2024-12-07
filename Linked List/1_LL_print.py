class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating the linked list
head = Node(10)
second = Node(20)
third = Node(30)

# Linking the nodes
head.next = second
second.next = third

# Function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")  # Indicates the end of the linked list

# Print the linked list
printLinkedList(head)
