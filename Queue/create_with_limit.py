# Creating with limit size

class Queue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.list = maxsize * [None]
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.list]
        return ' '.join(values)

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxsize:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            return 'The Queue is full. Cannot insert any elements'
        else:
            if self.top + 1 == self.maxsize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.list[self.top] = value
            return 'The element has been inserted'

    def dequeue(self):
        if self.isEmpty():
            return 'The Queue is empty'
        else:
            elem = self.list[self.start]
            start = self.start
            if self.start + 1 == self.maxsize:
                self.start = 0
            elif self.start == self.top:
                self.start = -1
                self.top = -1
            else:
                self.start += 1
            self.list[start] = None
            return elem

    def peek(self):
        if self.isEmpty():
            return 'The Queue is empty'
        else:
            elem = self.list[self.start]
            return elem

    def delete(self):
        self.list = self.maxsize * [None]
        self.start = -1
        self.top = -1


customqueue = Queue(5)
# print(customqueue.isEmpty())
customqueue.enqueue(1)
# customqueue.enqueue(2)
# customqueue.enqueue(3)
# print(customqueue)
print(customqueue.dequeue())
print(customqueue)
customqueue.enqueue(4)
# customqueue.enqueue(5)
# customqueue.enqueue(6)
print(customqueue)
# print(customqueue.peek())
# print(customqueue.isEmpty())
# print(customqueue.isFull())
# customqueue.delete()
# print(customqueue)