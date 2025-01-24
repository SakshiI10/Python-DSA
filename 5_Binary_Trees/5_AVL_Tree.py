# Study the code 

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    # Get the height of a node
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Get the balance factor of a node
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Perform a right rotation
    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    # Perform a left rotation
    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    # Insert a key into the AVL tree
    def insert(self, root, key):
        # Step 1: Perform normal BST insertion
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2: Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3: Get the balance factor to check if this node is unbalanced
        balance = self.get_balance(root)

        # Step 4: If the node is unbalanced, perform rotations
        # Case 1 - Left Left (LL)
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Case 2 - Right Right (RR)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Case 3 - Left Right (LR)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Case 4 - Right Left (RL)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    # Print the tree (Inorder Traversal)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

if __name__ == "__main__":
    avl = AVLTree()
    root = None

    # Inserting elements
    nums = [50, 20, 60, 10, 8, 15, 32, 46, 11, 38]
    for num in nums:
        root = avl.insert(root, num)

    print("Inorder traversal of the AVL tree:")
    avl.inorder(root)
