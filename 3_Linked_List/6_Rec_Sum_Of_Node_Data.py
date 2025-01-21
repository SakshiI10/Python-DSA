class Node:
    def __init__(self, data):
        # Initialize a node with the given data and set the next pointer to None
        self.data = data        #attribute of the Node class
        self.next = None        #attribute of the Node class

class LinkedList:
    def __init__(self):
        # Initialize the linked list with an empty head
        self.head = None        #attribute of the LinkedList class and reference to first node in the linked list

def Rec_sumNode(head):
    if head is None:
        return 0
    return head.data + Rec_sumNode(head.next)

ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)

print("Sum of Nodes: ",Rec_sumNode(ll.head))