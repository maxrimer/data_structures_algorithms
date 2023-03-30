# insert into DLL

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

    # Inserting node
    def createDLL(self, nodevalue):
        node = Node(nodevalue)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
        return 'The DLL id created successfully'

    # insert a node
    def insertDLL(self, value, location):
        if not self.head:
            return 'The list is empty'
        else:
            newnode = Node(value=value)
            if location == 0:
                newnode.prev = None
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode
            elif location == -1:
                newnode.next = None
                newnode.prev = self.tail
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                newnode.next = nextnode
                newnode.prev = tempnode
                tempnode.next = newnode
                nextnode.prev = newnode
                if tempnode == self.tail:
                    newnode.next = None
                    newnode.prev = self.tail
                    self.tail.next = newnode
                    self.tail = newnode

    # Traversing through DLL
    def traverseDLL(self):
        if not self.head:
            print('No elements to display')
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.next

    # Reverse traversal
    def reversetraverseDLL(self):
        if not self.head:
            print('No elements to display')
        else:
            tempnode = self.tail
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.prev


doublyLL = DoublyLinkedList()
doublyLL.createDLL(10)
doublyLL.insertDLL(0,0)
doublyLL.insertDLL(1,1)
doublyLL.insertDLL(2,2)
doublyLL.insertDLL(20,-1)
print([node.value for node in doublyLL])
doublyLL.traverseDLL()
print('*'*7)
doublyLL.reversetraverseDLL()