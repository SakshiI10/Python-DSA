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

def length1(head):
    if head is None:
        return 0
    count = 1
    temp=head.next

    while temp!=head:
        count += 1
        temp=temp.next
    return count

def length2(head):
    if head is None:
        return "EMPTY LIST"
    
    count=0
    temp=head

    while(True):
        count += 1
        temp=temp.next
        if temp==head:
            break
    return count

# Directly initialize the nodes
head = Node(1)  # First node (head)
second = Node(2)
third = Node(3)
fourth = Node(4)

# Connect the nodes to form a circular linked list
head.next = second
second.next = third
third.next = fourth
fourth.next = head  # Link the last node back to the head to make it circular

# Print the circular linked list
printList(head)
print("Length of CLL is: ",length1(head))
print("Length of CLL using do-while is: ",length2(head))