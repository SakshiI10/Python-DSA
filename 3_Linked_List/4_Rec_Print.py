class Node:
    def __init__(self, data):
        # Initialize a node with the given data and set the next pointer to None
        self.data = data        #attributes of the Node class
        self.next = None        #attributes of the Node class

class LinkedList:
    def __init__(self):
        # Initialize the linked list with an empty head
        self.head = None        #pointer

def Rec_print(head):
    if head is None:
        print("None")
        return
    
    print(head.data, end="->")  #head.data and head.next is an attribute
    Rec_print(head.next)

ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)

Rec_print(ll.head)