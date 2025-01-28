class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:
        return root
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root

    # Traverse the tree to find the node to be deleted
    # If the key is smaller, go to the left subtree
    if key < root.val:
        root.left = deleteNode(root.left, key)  
    # If the key is larger, go to the right subtree
    elif key > root.val:
        root.right = deleteNode(root.right, key) 
    else:
        # Node with only one child or no child (case for 0 or 1 child)
        # Case 1: No children
        if root.left is None and root.right is None:
            return None
        # Case 2: Only right child
        elif root.left is None:
            return root.right
        # Case 3: Only left child
        elif root.right is None:
            return root.left

        # Node with two children (case for 2 children):
        # Get the inorder successor (smallest in the right subtree) or 2 way is to find lergest in left subtree
        temp = minValueNode(root.right)

        # Copy the inorder successor's value to this node (root node now holds the smallest value)
        root.val = temp.val

        # Delete the inorder successor (since its value is now copied to the root)
        root.right = deleteNode(root.right, temp.val)

    return root

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)  
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
print("Inorder traversal before deletion:")
inorder(r)
print()
r = deleteNode(r, 50)
print("Inorder traversal after deleting 50:")
inorder(r)