class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize the linked list with an empty head
        self.head = None

def reverse_list(head):
    if head is None or head.next is None:
        return head
    
    # Initialize three reference: curr, prev and next
    prev = None
    curr = head
    next=head.next

    while curr:
        curr.next=prev
        prev = curr
        curr = next
        if next:
            next=next.next

    # Return the head of reversed linked list
    return prev

def Rec_print(head):
    if head is None:
        print("None")
        return
    
    print(head.data, end="->") 
    Rec_print(head.next)

ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(5)

print("Given Linked list:", end="")
Rec_print(ll.head)

head = reverse_list(ll.head)

print("Reversed Linked List:", end="")
Rec_print(head)