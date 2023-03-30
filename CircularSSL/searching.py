# Creating CircularSSL

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularSLinkedList:
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

    # Creation of CircularSSL
    def create_CircularSSL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = node
        return 'The CSLL has been created'

    # Inserting values into CSSL
    def insert_CSLL(self, value, location):
        if not self.head:
            return 'The CSLL does not exist'
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == -1:
                new_node.next = self.tail.next
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                nextnode = temp_node.next
                temp_node.next = new_node
                new_node.next = nextnode
                if temp_node == self.tail:
                    self.tail = new_node
            return 'The insertion has been completed'

    # Traversing
    def traverse_CSLL(self):
        if not self.head:
            return 'The linked list does not exist'
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    break

    # Searching a value in CSLL
    def search_CSLL(self, value):
        if not self.head:
            return 'The list does not exist'
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == value:
                    return temp_node.value
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    return 'The value does not exist in the list'




linked_list = CircularSLinkedList()
print(linked_list.create_CircularSSL(1))
linked_list.insert_CSLL(0,0)
linked_list.insert_CSLL(2,2)
linked_list.insert_CSLL(3,3)
linked_list.insert_CSLL(4,4)
linked_list.insert_CSLL(5,5)
linked_list.insert_CSLL(6,-1)

# print([node.value for node in linked_list])
# linked_list.traverse_CSLL()
print(linked_list.search_CSLL(10))