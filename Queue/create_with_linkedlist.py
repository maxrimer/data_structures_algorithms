# Creating a Queue using a linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currnode = self.head
        while currnode:
            yield currnode
            currnode = currnode.next


class Queue:
    def __init__(self):
        self.list = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.list]
        return ' '.join(values)

    def isEmpty(self):
        if not self.list.head:
            return True
        return False

    def enqueue(self, value):
        node = Node(value)
        if self.isEmpty():
            self.list.head = node
            self.list.tail = node
            return 'The element has been inserted successfully'
        else:
            self.list.tail.next = node
            self.list.tail = node
            return 'The element has been inserted successfully'

    def dequeue(self):
        if self.isEmpty():
            return 'The Queue is empty'
        else:
            element = self.list.head.value
            self.list.head = self.list.head.next
            return element

    def peek(self):
        if self.isEmpty():
            return 'The Queue is empty'
        else:
            return self.list.head.value

    def delete(self):
        self.list.head = None




customqueue = Queue()
customqueue.enqueue(1)
customqueue.enqueue(2)
customqueue.enqueue(3)
print(customqueue)
customqueue.delete()
print(customqueue)