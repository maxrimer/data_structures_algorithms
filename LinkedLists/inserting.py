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


singlylinkedlist = SLinkedList()
singlylinkedlist.insertSSL(0)
singlylinkedlist.insertSSL(1, -1)
singlylinkedlist.insertSSL(2, -1)
singlylinkedlist.insertSSL(3, -1)
singlylinkedlist.insertSSL(4, -1)
singlylinkedlist.insertSSL(5, -1)
singlylinkedlist.insertSSL(6, 3)
print([node.value for node in singlylinkedlist])
