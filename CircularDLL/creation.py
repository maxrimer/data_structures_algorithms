# Creating a Circular Doubly Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


# Create a list class
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # creating a list
    def createCDLL(self, nodevalue):
        node = Node(nodevalue)
        self.head = node
        self.tail = node
        node.next = node
        node.prev = node
        return 'The CDLL has been created successfully'


circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(5)
print([node.value for node in circularDLL])
