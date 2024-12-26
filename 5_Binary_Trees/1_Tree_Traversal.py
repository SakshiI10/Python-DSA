class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

# Inorder Traversal
def printInOrder(node):
    if node:
        # Traverse left subtree
        printInOrder(node.left)
        # Visit node
        print(node.data, end=" ")
        # Traverse right subtree
        printInOrder(node.right)

# Preorder Traversal
def printPreOrder(node):
    if node:
        # Visit node
        print(node.data, end=" ")
        # Traverse left subtree
        printPreOrder(node.left)
        # Traverse right subtree
        printPreOrder(node.right)

# Postorder Traversal
def printPostOrder(node):
    if node:
        # Traverse left subtree
        printPostOrder(node.left)
        # Traverse right subtree
        printPostOrder(node.right)
        # Visit node
        print(node.data, end=" ")

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(25)
    root.right = Node(30)
    root.left.left = Node(20)
    root.left.right = Node(35)
    root.right.left = Node(15)
    root.right.right = Node(45)

    print("Inorder Traversal: ", end="")
    printInOrder(root)
    print()

    print("Preorder Traversal: ", end="")
    printPreOrder(root)
    print()

    print("Postorder Traversal: ", end="")
    printPostOrder(root)
    print()
