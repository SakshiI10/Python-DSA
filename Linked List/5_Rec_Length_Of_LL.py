class Node:
    def __init__(self, data):
        # Initialize a node with the given data and set the next pointer to None
        self.data = data        #attributes of the Node class
        self.next = None        #attributes of the Node class

class LinkedList:
    def __init__(self):
        # Initialize the linked list with an empty head
        self.head = None        #pointer

def Rec_count(head):
    if head is None:
        return 0
    return 1 + Rec_count(head.next)

ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)

print("Length of Linked List: ",Rec_count(ll.head))