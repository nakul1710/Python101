# Append function in SLL (singly-linked-list)
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

# Example usage:
my_list = SinglyLinkedList()
my_list.head = node4  # Attach existing nodes
my_list.append(30)
