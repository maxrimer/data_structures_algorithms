# Create stack with size limit

class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return 'The size limit is reached'
        else:
            self.list.append(value)
            return 'The element has been successfully inserted'

    def pop(self):
        if self.isEmpty():
            return 'The stack is empty'
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return 'The stack is empty'
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None


customstack = Stack(5)
customstack.push(5)
customstack.push(6)
customstack.push(7)
customstack.push(8)
print(customstack)
print('*'*10)
print(customstack.isFull())
print('*'*10)
print(customstack.isEmpty())
print('*'*10)
print(customstack.peek())