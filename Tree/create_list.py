# creating a binary tree using python list

class BinaryTree:
    def __init__(self, size):
        self.list = size * [None]
        self.lastusedindex = 0
        self.maxsize = size

    def insertnode(self, value):
        if self.lastusedindex + 1 == self.maxsize:
            return 'The tree is already full'
        self.list[self.lastusedindex+1] = value
        self.lastusedindex += 1
        return 'The value has been successfully inserted'

    def searchnode(self, value):
        for i in range(len(self.list)):
            if self.list[i] == value:
                return 'Found'
        return 'Not found'

    def preordertraversal(self, index):
        if index > self.lastusedindex:
            return
        print(self.list[index])
        self.preordertraversal(index*2)
        self.preordertraversal(index*2+1)

    def inordertraversal(self, index):
        if index > self.lastusedindex:
            return
        self.inordertraversal(index*2)
        print(self.list[index])
        self.inordertraversal(index*2+1)

    def postordertraversal(self, index):
        if index > self.lastusedindex:
            return
        self.postordertraversal(index*2)
        self.postordertraversal(index*2+1)
        print(self.list[index])

    def levelordertraversal(self, index):
        for i in range(index, self.lastusedindex+1):
            print(self.list[i])

    def deletenode(self, value):
        if self.lastusedindex == 0:
            return 'There are no elements in a binary tree'
        for i in range(1, self.lastusedindex+1):
            if self.list[i] == value:
                self.list[i] = self.list[self.lastusedindex]
                self.list[self.lastusedindex] = None
                self.lastusedindex -= 1
                return 'The node has been successfully deleted'
        return 'There is no such node in a binary tree'

    def deleteentiretree(self):
        self.list = None
        return 'The list has been successfully deleted'


binarytree = BinaryTree(9)
binarytree.insertnode('Drinks')
binarytree.insertnode('Hot')
binarytree.insertnode('Cold')
binarytree.insertnode('Tea')
binarytree.insertnode('Coffee')
binarytree.insertnode('Cola')
binarytree.insertnode('Fanta')
binarytree.insertnode('Green')
# binarytree.preordertraversal(1)
# binarytree.inordertraversal(1)
# binarytree.postordertraversal(1)
# print(binarytree.deletenode('Cold')
print(binarytree.deleteentiretree())
binarytree.levelordertraversal(1)
