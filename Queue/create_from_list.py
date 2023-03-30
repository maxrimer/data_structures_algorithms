# Creating Queue from a list

class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if not self.items:
            return True
        return False

    def enqueue(self, value):
        self.items.append(value)
        return 'The element is inserted at the end of Queue'

    def dequeue(self):
        if self.isEmpty():
            return 'The Queue is empty'
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return 'The Queue is empty'
        else:
            return self.items[0]

    def delete(self):
        self.items = None


customqueue = Queue()
print(customqueue.isEmpty())
customqueue.enqueue(1)
customqueue.enqueue(2)
customqueue.enqueue(3)
print(customqueue)
print(customqueue.isEmpty())
customqueue.dequeue()
print(customqueue.peek())
customqueue.delete()