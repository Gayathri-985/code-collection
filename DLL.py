class Node:
    """Class to represent a node in the doubly linked list."""
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node


class DoublyLinkedList:
    """Class to represent a doubly linked list."""
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def is_empty(self):
        """Check if the doubly linked list is empty."""
        return self.head is None

    def append(self, data):
        """Add a node to the end of the doubly linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def prepend(self, data):
        """Add a node to the beginning of the doubly linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_after(self, prev_data, data):
        """Insert a node after a specific node."""
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        if current is None:
            print(f"Node with data {prev_data} not found.")
            return
        new_node = Node(data)
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def delete_node(self, data):
        """Delete a node with a specific value."""
        if self.head is None:
            print("List is empty.")
            return

        current = self.head

        # If the head is the node to be deleted
        if current.data == data:
            if current.next:
                current.next.prev = None
            self.head = current.next
            return

        # Search for the node to delete
        while current and current.data != data:
            current = current.next

        if current is None:
            print(f"Node with data {data} not found.")
            return

        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

    def traverse_forward(self):
        """Print all elements in the doubly linked list (forward direction)."""
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        """Print all elements in the doubly linked list (backward direction)."""
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" <- ")
            current = current.prev
        print("None")

    def reverse(self):
        """Reverse the doubly linked list."""
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            if current.prev is None:
                self.head = current
            current = current.prev

    def length(self):
        """Return the length of the doubly linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def search(self, data):
        """Search for a node with a specific value."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


# Example Usage
if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("Appending elements to the doubly linked list:")
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.traverse_forward()

    print("\nPrepending an element:")
    dll.prepend(5)
    dll.traverse_forward()

    print("\nInserting after an element:")
    dll.insert_after(20, 25)
    dll.traverse_forward()

    print("\nTraversing backward:")
    dll.traverse_backward()

    print("\nDeleting a specific node:")
    dll.delete_node(20)
    dll.traverse_forward()

    print("\nReversing the doubly linked list:")
    dll.reverse()
    dll.traverse_forward()

    print("\nLength of the doubly linked list:", dll.length())

    print("\nSearching for an element (25):", dll.search(25))
    print("Searching for an element (40):", dll.search(40))

    print("\nFinal Doubly Linked List (Forward):")
    dll.traverse_forward()
