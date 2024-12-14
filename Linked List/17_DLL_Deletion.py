class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

# Create the doubly linked list
head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)

# Linking the nodes
head.next = second
second.prev = head
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third

def delete_first(head):
    if head is None:  # If the list is empty
        print("Nothing to delete")
        return None
    if head.next is None:  # If there is only one node
        return None
    else:  # More than one node
        temp = head  # Store the current head
        head = head.next  # Move the head to the next node
        head.prev = None  # Remove the backward link
        del temp  # Free the old head
        return head  # Return the updated head

def delete_end(head):
    if head is None or head.next is None:
        return None
    
    temp=head
    while temp.next.next is None:
        temp=temp.next

    temp.next=None
    return head

def printDLL(head):
    if head is None:
        print("Empty Linked List")
        return

    temp = head
    while temp:
        print(temp.data, end=" <=> ")
        temp = temp.next
    print("None")  # Indicates the end of the list

head = delete_first(head)
printDLL(head)
head = delete_end(head)
printDLL(head)

