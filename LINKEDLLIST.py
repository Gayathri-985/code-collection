class Node:
    """Class to represent a node in the linked list."""
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.next = None  # Pointer to the next node


class LinkedList:
    """Class to represent a singly linked list."""
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head is None

    def append(self, data):
        """Add a node to the end of the linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a node to the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
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
        current.next = new_node

    def delete_node(self, data):
        """Delete a node with a specific value."""
        if self.head is None:
            print("List is empty.")
            return

        # If the head is the node to be deleted
        if self.head.data == data:
            self.head = self.head.next
            return

        # Search for the node to delete
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next is None:
            print(f"Node with data {data} not found.")
        else:
            current.next = current.next.next

    def reverse(self):
        """Reverse the linked list."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def traverse(self):
        """Print all elements in the linked list."""
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, data):
        """Search for a node with a specific value."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def length(self):
        """Return the length of the linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get_nth(self, index):
        """Get the data of the nth node (0-based index)."""
        if index < 0:
            print("Index must be non-negative.")
            return None
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        print(f"Index {index} out of range.")
        return None

    def delete_at_position(self, index):
        """Delete a node at a specific position (0-based index)."""
        if index < 0:
            print("Index must be non-negative.")
            return

        if self.head is None:
            print("List is empty.")
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        count = 0
        while current.next and count < index - 1:
            count += 1
            current = current.next

        if current.next is None:
            print(f"Index {index} out of range.")
        else:
            current.next = current.next.next


# Example Usage
if __name__ == "__main__":
    linked_list = LinkedList()

    print("Appending elements to the linked list:")
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.traverse()

    print("\nPrepending an element:")
    linked_list.prepend(5)
    linked_list.traverse()

    print("\nInserting after an element:")
    linked_list.insert_after(20, 25)
    linked_list.traverse()

    print("\nDeleting a specific node:")
    linked_list.delete_node(20)
    linked_list.traverse()

    print("\nReversing the linked list:")
    linked_list.reverse()
    linked_list.traverse()

    print("\nLength of the linked list:", linked_list.length())

    print("\nSearching for an element (25):", linked_list.search(25))
    print("Searching for an element (40):", linked_list.search(40))

    print("\nGetting the 2nd element (0-based index):", linked_list.get_nth(2))

    print("\nDeleting node at position 2:")
    linked_list.delete_at_position(2)
    linked_list.traverse()

    print("\nFinal Linked List:")
    linked_list.traverse()
