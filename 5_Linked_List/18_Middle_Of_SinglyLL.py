class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Function to add a new node at the end of the list
    def append(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse the list to the last node
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        # Set the next of the last node to the new node
        current_node.next = new_node

    # Function to print the middle of the linked list
    def print_middle(self):
        slow = self.head
        fast = self.head

        if not self.head:
            print("The linked list is empty.")
            return

        # Move `fast_ptr` two steps and `slow_ptr` one step at a time
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # When `fast_ptr` reaches the end, `slow_ptr` is at the middle
        print("The middle element is:", slow.data)

    # Function to print the entire linked list
    def print_list(self):
        if self.head is None:
            print("The linked list is empty.")
            return
        
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
print("Linked List:")
ll.print_list()
ll.print_middle()

# Time complexity: O(n)
# Space complexity: O(1)