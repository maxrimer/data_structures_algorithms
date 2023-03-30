# Creating a Binary Tree using linked list
from create_queue_with_linkedlist import Queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


def preordertraverse(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preordertraverse(rootnode.leftchild)
    preordertraverse(rootnode.rightchild)


def inordertraverse(rootnode):
    if not rootnode:
        return
    inordertraverse(rootnode.leftchild)
    print(rootnode.data)
    inordertraverse(rootnode.rightchild)


def postordertraverse(rootnode):
    if not rootnode:
        return
    postordertraverse(rootnode.leftchild)
    postordertraverse(rootnode.rightchild)
    print(rootnode.data)


def levelordertraversal(rootnode):
    if not rootnode:
        return
    else:
        customqueue = Queue()
        customqueue.enqueue(rootnode)
        while not(customqueue.isEmpty()):
            root = customqueue.dequeue()
            print(root.data)
            if root.leftchild:
                customqueue.enqueue(root.leftchild)

            if root.rightchild:
                customqueue.enqueue(root.rightchild)


def searchBT(rootnode, nodevalue):
    if not rootnode:
        return
    else:
        customqueue = Queue()
        customqueue.enqueue(rootnode)
        while not(customqueue.isEmpty()):
            root = customqueue.dequeue()
            if root.data == nodevalue:
                return 'Success'

            if root.leftchild:
                customqueue.enqueue(root.leftchild)

            if root.rightchild:
                customqueue.enqueue(root.rightchild)
        return 'Value not found'


def insertnode(rootnode, newnode):
    if not rootnode:
        rootnode = newnode
    else:
        customqueue = Queue()
        customqueue.enqueue(rootnode)
        while not(customqueue.isEmpty()):
            root = customqueue.dequeue()
            if root.leftchild:
                customqueue.enqueue(root.leftchild)
            else:
                root.leftchild = newnode
                return 'Node successfully inserted'
            if root.rightchild:
                customqueue.enqueue(root.rightchild)
            else:
                root.rightchild = newnode
                return 'Node successfully inserted'


def finddeepestnode(rootnode):
    if not rootnode:
        return
    else:
        customqueue = Queue()
        customqueue.enqueue(rootnode)
        while not(customqueue.isEmpty()):
            root = customqueue.dequeue()
            if root.leftchild:
                customqueue.enqueue(root.leftchild)
            if root.rightchild:
                customqueue.enqueue(root.rightchild)
        return root


def deletedeepestnode(rootnode, deepestnode):
    if not rootnode:
        return
    else:
        customqueue = Queue()
        customqueue.enqueue(rootnode)
        while not (customqueue.isEmpty()):
            root = customqueue.dequeue()
            if root is deepestnode:
                root = None
                return
            if root.rightchild:
                if root.rightchild is deepestnode:
                    root.rightchild = None
                    return
                else:
                    customqueue.enqueue(root.rightchild)
            if root.leftchild:
                if root.leftchild is deepestnode:
                    root.leftchild = None
                    return
                else:
                    customqueue.enqueue(root.leftchild)


def deletenodeBT(rootnode, node):
    if not rootnode:
        return 'The tree does not exist'
    else:
        customqueue = Queue()
        customqueue.enqueue(rootnode)
        while not (customqueue.isEmpty()):
            root = customqueue.dequeue()
            if root.data == node:
                tempnode = finddeepestnode(rootnode)
                root.data = tempnode.data
                deletedeepestnode(rootnode, tempnode)
                return 'The node has been successfully deleted'

            if root.leftchild:
                customqueue.enqueue(root.leftchild)

            if root.rightchild:
                customqueue.enqueue(root.rightchild)
        return 'Failed to delete a node'


def deleteBT(rootnode):
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None


binarytree = TreeNode('Drinks')
hot = TreeNode('Hot')
cold = TreeNode('Cold')
binarytree.leftchild = hot
binarytree.rightchild = cold
# preordertraverse(binarytree)
# inordertraverse(binarytree)
fanta = TreeNode('Fanta')
cola = TreeNode('Cola')
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
hot.leftchild = tea
hot.rightchild = coffee
cold.leftchild = cola
cold.rightchild = fanta
# postordertraverse(binarytree)
# levelordertraversal(binarytree)
# print(searchBT(binarytree, 'Mango'))
# fanta = TreeNode('Fanta')
# cola = TreeNode('Coca Cola')
# print(insertnode(binarytree, cola))
# print(insertnode(binarytree, fanta))
# levelordertraversal(binarytree)
# binarytreedn = finddeepestnode(binarytree)
# deletedeepestnode(binarytree, dn)
# levelordertraversal(binarytree)
# print(deletenodeBT(binarytree, 'Milk'))
# levelordertraversal(binarytree)
deleteBT(binarytree)
levelordertraversal(binarytree)




