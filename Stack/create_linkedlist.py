# Creating a stack using a linked list

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        currnode = self.head
        while currnode:
            yield currnode
            currnode = currnode.next


class Stack:
    def __init__(self):
        self.Linkedlist = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.Linkedlist]
        return '\n'.join(values)

    def isEmpty(self):
        if not self.Linkedlist.head:
            return True
        return False

    def push(self, value):
        node = Node(value)
        node.next = self.Linkedlist.head
        self.Linkedlist.head = node

    def pop(self):
        if self.isEmpty():
            return 'The stack is empty. No elements to remove'
        else:
            nodevalue = self.Linkedlist.head.value
            self.Linkedlist.head = self.Linkedlist.head.next
            return nodevalue

    def peek(self):
        if self.isEmpty():
            return 'The stack is empty. No elements to remove'
        else:
            nodevalue = self.Linkedlist.head.value
            return nodevalue

    def delete(self):
        self.Linkedlist.head = None


llstack = Stack()
llstack.push(1)
llstack.push(2)
llstack.push(3)
llstack.push(4)
llstack.push(5)
llstack.push(6)
llstack.push(7)
llstack.push(8)
print(llstack)
# for _ in range(5):
#     llstack.pop()
# print('*'*10)
# print(llstack)

while not llstack.isEmpty():
    llstack.pop()
    llstack.pop()
# print('*'*10)
# print(llstack)