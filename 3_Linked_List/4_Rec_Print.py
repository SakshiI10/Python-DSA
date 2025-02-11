class Node:
    def __init__(self, data):
        # Initialize a node with the given data and set the next pointer to None
        self.data = data        #attribute of the Node class
        self.next = None        #attribute of the Node class

class LinkedList:
    def __init__(self):
        # Initialize the linked list with an empty head
        self.head = None        #attribute of the LinkedList class and reference to first node in the linked list

def Rec_print(head):
    if head is None:
        print("None")
        return
    
    print(head.data, end=" -> ")  #head.data and head.next is an attribute
    Rec_print(head.next)

LinkedList()
LinkedList.head = Node(1)
LinkedList.head.next = Node(2)
LinkedList.head.next.next = Node(3)
LinkedList.head.next.next.next = Node(4)

Rec_print(LinkedList.head)