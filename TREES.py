# Define a class for a Node in the tree
class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.left = None  # Left child
        self.right = None  # Right child

# Define a class for the Binary Tree
class BinaryTree:
    def __init__(self):
        self.root = None  # Root node of the tree

    # Insert a node into the tree (Binary Search Tree structure)
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.data:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        elif value > current.data:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

    # Preorder Traversal: Root -> Left -> Right
    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Inorder Traversal: Left -> Root -> Right
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    # Postorder Traversal: Left -> Right -> Root
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    # Search for a value in the tree
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, current, value):
        if current is None:
            return False
        if current.data == value:
            return True
        elif value < current.data:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)

# Example Usage
if __name__ == "__main__":
    # Create a BinaryTree instance
    tree = BinaryTree()

    # Insert elements into the tree
    elements = [50, 30, 70, 20, 40, 60, 80]
    for elem in elements:
        tree.insert(elem)

    print("Tree Traversals:")
    print("\nPreorder Traversal:")
    tree.preorder(tree.root)

    print("\n\nInorder Traversal:")
    tree.inorder(tree.root)

    print("\n\nPostorder Traversal:")
    tree.postorder(tree.root)

    print("\n\nSearch for a value:")
    value_to_search = 60
    if tree.search(value_to_search):
        print(f"Value {value_to_search} found in the tree!")
    else:
        print(f"Value {value_to_search} not found in the tree!")
