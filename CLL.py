class Node:
    """Class to represent a node in the circular linked list."""
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.next = None  # Pointer to the next node


class CircularLinkedList:
    """Class to represent a circular linked list."""
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def is_empty(self):
        """Check if the circular linked list is empty."""
        return self.head is None

    def append(self, data):
        """Add a node to the end of the circular linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def prepend(self, data):
        """Add a node to the beginning of the circular linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, target_data, data):
        """Insert a node after a specific node in the circular linked list."""
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while True:
            if current.data == target_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            if current == self.head:
                break
        print(f"Node with data {target_data} not found.")

    def delete_node(self, target_data):
        """Delete a node with a specific value."""
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        prev = None

        # If the head node is the one to delete
        if current.data == target_data:
            if current.next == self.head:  # If there is only one node
                self.head = None
                return
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return

        # Search for the node to delete
        while current.next != self.head:
            prev = current
            current = current.next
            if current.data == target_data:
                prev.next = current.next
                return

        print(f"Node with data {target_data} not found.")

    def traverse(self):
        """Traverse and print all elements in the circular linked list."""
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

    def search(self, data):
        """Search for a node with a specific value."""
        if self.head is None:
            return False
        current = self.head
        while True:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def length(self):
        """Return the number of nodes in the circular linked list."""
        if self.head is None:
            return 0
        count = 0
        current = self.head
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count


# Example Usage
if __name__ == "__main__":
    cll = CircularLinkedList()

    print("Appending elements to the circular linked list:")
    cll.append(10)
    cll.append(20)
    cll.append(30)
    cll.traverse()

    print("\nPrepending an element:")
    cll.prepend(5)
    cll.traverse()

    print("\nInserting after an element:")
    cll.insert_after(20, 25)
    cll.traverse()

    print("\nDeleting a specific node:")
    cll.delete_node(20)
    cll.traverse()

    print("\nLength of the circular linked list:", cll.length())

    print("\nSearching for elements:")
    print("25 found:", cll.search(25))
    print("40 found:", cll.search(40))

    print("\nFinal Circular Linked List:")
    cll.traverse()
