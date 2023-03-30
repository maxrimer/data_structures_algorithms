# Creating a stack from list

class Stack:
    def __init__(self):
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

    def push(self, value):
        self.list.append(value)
        return 'The element has been appended'

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


customstack = Stack()
customstack.push(5)
customstack.push(6)
customstack.push(7)
print(customstack)
print('*'*10)
customstack.delete()