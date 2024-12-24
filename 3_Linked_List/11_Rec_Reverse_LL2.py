class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def reverse_list2(head, prev):
    if head is None:
        return prev
    
    curr = reverse_list2(head.next, head)
    head.next=prev

    return curr

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = reverse_list2(head, prev=None)   
    print_list(head)