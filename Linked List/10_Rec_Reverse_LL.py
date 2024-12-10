class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def reverse_list(head):
    if head is None or head.next is None:
        return head

    # Reverse the rest of the list
    new_Head = reverse_list(head.next)
    
    # Make the current head the last node
    head.next.next = head
    
    # Update the next of current head to None
    head.next = None
    
    # Return the new head of the reversed list
    return new_Head

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

    head = reverse_list(head)   
    print_list(head)

# After executing this line: new_Head = reverse_list(head.next), the head will come at last node and it will return to second last.
#After returning to second last this line will work: head.next.next = head.