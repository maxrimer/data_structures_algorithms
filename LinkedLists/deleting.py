# insering a value into a singly linked list


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Printing
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Insering
    def insertSSL(self, value: int, location=0):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == -1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
                if temp_node == self.tail:
                    self.tail = new_node

    def traverseSSL(self):
        if not self.head:
            print('No elements')
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next

    # Searching for a value in a SSL
    def searchingSSL(self, nodevalue):
        if not self.head:
            return 'No elements'
        else:
            node = self.head
            while node:
                if node.value == nodevalue:
                    return node.value
                node = node.next
            return 'No such element'

    def deletingSSL(self, location):
        if not self.head:
            return 'No elements'
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                if nextnode == self.tail:
                    tempnode.next = None
                    self.tail = tempnode
                tempnode.next = nextnode.next


    def deleteintireSSL(self):
        if not self.head:
            return 'The list is empty'
        else:
            self.head = None
            self.tail = None


singlylinkedlist = SLinkedList()
singlylinkedlist.insertSSL(0)
singlylinkedlist.insertSSL(1, -1)
singlylinkedlist.insertSSL(2, -1)
singlylinkedlist.insertSSL(3, -1)
singlylinkedlist.insertSSL(4, -1)
singlylinkedlist.insertSSL(5, -1)
singlylinkedlist.insertSSL(6, 3)
print([node.value for node in singlylinkedlist])
# singlylinkedlist.traverseSSL()
#print(singlylinkedlist.searchingSSL(2))
# singlylinkedlist.deletingSSL(5)
singlylinkedlist.deleteintireSSL()
print([node.value for node in singlylinkedlist])
