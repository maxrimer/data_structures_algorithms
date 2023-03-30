# Create 3 stacks from one list

class MultiClass:
    def __init__(self, stacksize):
        self.numstacks = 3
        self.custlist = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize

    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        return False

    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        return False

    def topindex(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

    def push(self, value, stacknum):
        if self.isFull(stacknum):
            return 'The stack is full!'
        else:
            self.sizes[stacknum] += 1
            self.custlist[self.topindex(stacknum)] = value

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return 'The stack is empty'
        else:
            value = self.custlist[self.topindex(stacknum)]
            self.custlist[self.topindex(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return 'The stack is empty'
        else:
            value = self.custlist[self.topindex(stacknum)]
            return value


customstack = MultiClass(6)
customstack.push(0, 0)
customstack.push(1, 0)
customstack.push(2, 0)
customstack.push(3, 1)
customstack.push(4, 1)
customstack.push(5, 2)
print(customstack.peek(1))