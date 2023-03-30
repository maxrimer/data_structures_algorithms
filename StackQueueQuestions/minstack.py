# Add min functionality to a stack

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        string = str(self.value)
        if self.next:
            string += ',' + str(self.next)
        return string


class Stack:
    def __init__(self):
        self.top = None
        self.minnode = None

    def min(self):
        if not self.minnode:
            return None
        return self.minnode.value

    def push(self, item):
        if self.minnode and (self.minnode.value < item):
            self.minnode = Node(self.minnode.value, self.minnode)
        else:
            self.minnode = Node(item, self.minnode)
        self.top = Node(item, self.top)

    def pop(self):
        if not self.top:
            return None
        self.minnode = self.minnode.next
        value = self.top.value
        self.top = self.top.next
        return value


customstack = Stack()
customstack.push(5)
print(customstack.min())
customstack.push(4)
customstack.push(7)
print(customstack.min())
customstack.push(2)
print(customstack.min())
print(customstack.pop())
print(customstack.pop())
print(customstack.pop())
print(customstack.min())




