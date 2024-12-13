class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

def insert_at_begin(head, val):
    new_node=Node(val)

    if head is None:
        head=new_node
        return head
    else:
        new_node.next=head
        head.prev=new_node
        head=new_node
        return head

def insert_at_end(head, val):
    new_node=Node(val)

    if head is None:
        head=new_node
        return head
    else:
        temp=head
        while temp.next is not None:
            temp=temp.next

        temp.next=new_node
        new_node.prev=temp
        return head
    
def printDLL(head):
    if head is None:
        print("Empty Linked List")

    temp = head
    while temp:
        print(temp.data, end=" <=> ")
        temp = temp.next
    print("None")

head=None
printDLL(head)
head=insert_at_begin(head, 1)
printDLL(head)
head=insert_at_begin(head, 2)
printDLL(head)
head=insert_at_end(head, 3)
printDLL(head)
head=insert_at_end(head, 4)
printDLL(head)
