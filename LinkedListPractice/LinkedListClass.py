# Creating a linked list class
from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


# Creating a linked list class
class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None

    def __iter__(self):
        tempnode = self.head
        while tempnode:
            yield tempnode
            tempnode = tempnode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)

    def __len__(self):
        result = 0
        tempnode = self.head
        while tempnode:
            result += 1
            tempnode = tempnode.next
        return result

    def add(self, value):
        if not self.head:
            newnode = Node(value)
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, min_val, max_val):
        self.head = None
        self.tail = None
        for _ in range(n):
            self.add(randint(min_val, max_val))
        return self


# newnode = Node(10)
# print(newnode)
if __name__ == '__main__':
    customll = LinkedList()
    customll.generate(10, 0, 99)
    print(customll)
    print(len(customll))
