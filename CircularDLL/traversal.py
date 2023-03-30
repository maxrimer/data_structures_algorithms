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

    # Insert a node
    def insertnodeCDLL(self, value, location):
        if not self.head:
            return 'The list is empty'
        else:
            newnode = Node(value)
            if location == 0:
                newnode.next = self.head
                newnode.prev = self.tail
                self.head.prev = newnode
                self.head = newnode
                self.tail.next = newnode
            elif location == -1:
                newnode.next = self.head
                newnode.prev = self.tail
                self.tail.next = newnode
                self.head.prev = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                if tempnode == self.tail:
                    newnode.next = self.head
                    newnode.prev = self.tail
                    self.tail.next = newnode
                    self.head.prev = newnode
                    self.tail = newnode
                else:
                    newnode.prev = tempnode
                    newnode.next = tempnode.next
                    newnode.next.prev = newnode
                    tempnode.next = newnode

    # traversal
    def traversalCDLL(self):
        if not self.head:
            print('The list is empty!')
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                if tempnode == self.tail:
                    break
                tempnode = tempnode.next

    # Reverse traversal
    def reversetraversalCDLL(self):
        if not self.head:
            print('The list is empty')
        else:
            tempnode = self.tail
            while tempnode:
                print(tempnode.value)
                if tempnode == self.head:
                    break
                tempnode = tempnode.prev


circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(5)
# print([node.value for node in circularDLL])
circularDLL.insertnodeCDLL(0,0)
circularDLL.insertnodeCDLL(1, 2)
circularDLL.insertnodeCDLL(10, -1)
print([node.value for node in circularDLL])
# circularDLL.traversalCDLL()
circularDLL.reversetraversalCDLL()