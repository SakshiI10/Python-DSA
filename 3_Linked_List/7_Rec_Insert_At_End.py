class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        # Initialize the linked list with an empty head
        self.head = None

def Rec_insert_end(head, data):
    if head is None:
        return Node(data)
    head.next=Rec_insert_end(head.next, data)
    return head

def Rec_print(head):
    if head is None:
        print("None")
        return
    
    print(head.data, end="->")  #head.data and head.next is an attribute
    Rec_print(head.next)

LinkedList()
LinkedList.head = Node(1)
LinkedList.head.next = Node(2)
LinkedList.head.next.next = Node(3)
LinkedList.head.next.next.next = Node(4)
LinkedList.head = Rec_insert_end(LinkedList.head, 5)
Rec_print(LinkedList.head)

# ll = LinkedList()
# ll.head = Node(1)
# ll.head.next = Node(2)
# ll.head.next.next = Node(3)
# ll.head.next.next.next = Node(4)
