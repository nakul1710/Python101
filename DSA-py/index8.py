#Singly linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# create linked list nodes
node1 = Node(5)
node2 = Node(10)
node3 = Node(7)
node4 = Node(8)

# link nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

print(node1)
print(node4.val)
print(node2.next)

# function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# print the list
print_linked_list(node1)


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

# Optionally, print the list to verify
print_linked_list(my_list.head)

# Traversal in (SLL)
# Fix: Make Traversal a method of SinglyLinkedList and use it properly

class SinglyLinkedList:

    def traversal(self):
        if self.head is None:
            print("SLL is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end=" -> " if curr.next else "\n")
                curr = curr.next

# Example usage:
my_trav_list = SinglyLinkedList()
my_trav_list.head = node1
my_trav_list.traversal()





