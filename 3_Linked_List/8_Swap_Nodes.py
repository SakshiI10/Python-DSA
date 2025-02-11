class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        # Initialize the linked list with an empty head
        self.head = None

def Swap_pairs(head):
    if head is None or head.next is None:
        return head
    
    temp=head.data
    head.data=head.next.data
    head.next.data=temp

    Swap_pairs(head.next.next)

    return head

def Rec_print(head):
    if head is None:
        print("None")
        return
    
    print(head.data, end=" -> ")  #head.data and head.next is an attribute
    Rec_print(head.next)

ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(5)
ll.head = Swap_pairs(ll.head)

Rec_print(ll.head)