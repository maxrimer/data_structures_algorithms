class StackPlate:
    def __init__(self, stacksize):
        self.stacksize = stacksize
        self.stacks = []

    def __str__(self):
        stacks = reversed(self.stacks)
        stacks = [str(x) for x in stacks]
        return '\n'.join(stacks)

    def push(self, item):
        if len(self.stacks) and len(self.stacks[-1]) < self.stacksize:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if not len(self.stacks):
            return None
        else:
            return self.stacks[-1].pop()

    def popat(self, stacknum):
        if not self.stacks[stacknum]:
            return None
        else:
            return self.stacks[stacknum].pop()


customstack = StackPlate(2)
customstack.push(1)
customstack.push(2)
customstack.push(3)
customstack.push(4)
customstack.push(5)
print(customstack.pop())
print(customstack.pop())
print(customstack.popat(0))