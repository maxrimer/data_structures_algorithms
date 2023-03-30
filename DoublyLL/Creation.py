# Creating Doubly Linked Lists
# Creating node
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


# Creating DLL
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # for printing values in the list

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Creation DLL
    def createDLL(self, nodevalue):
        node = Node(nodevalue)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
        return 'The DLL id created successfully'


doublyLL = DoublyLinkedList()
doublyLL.createDLL(10)

print([node.value for node in doublyLL])