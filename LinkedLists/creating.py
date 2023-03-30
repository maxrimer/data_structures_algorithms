# creating a singly linked list


class Node:
    def __int__(self, value):
        self.value = value
        self.next = None


class SLinkedList:
    def __int__(self):
        self.head = None
        self.tail = None


SinglyLinkedList = SLinkedList()
node1 = Node(1)
node2 = Node(2)
SinglyLinkedList.head = node1
SinglyLinkedList.head.next = node2
SinglyLinkedList.tail = node2
