class Stack:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if not self.list:
            return None
        return self.list.pop()


class QueueViaStack:
    def __init__(self):
        self.instack = Stack()
        self.outstack = Stack()

    def enqueuue(self, item):
        self.instack.push(item)

    def dequeue(self):
        if len(self.instack) == 0:
            return None
        else:
            while len(self.instack):
                self.outstack.push(self.instack.pop())
            result = self.outstack.pop()
            while len(self.outstack):
                self.instack.push(self.outstack.pop())
            return result


customqueue = QueueViaStack()
customqueue.enqueuue(1)
customqueue.enqueuue(2)
customqueue.enqueuue(3)
customqueue.enqueuue(4)
customqueue.enqueuue(5)
print(customqueue.dequeue())
print(customqueue.dequeue())