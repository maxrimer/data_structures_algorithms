# create a bst using linked list
from create_queue_with_linkedlist import Queue


class BST:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


def insertnode(rootnode, nodevalue):
    if not rootnode.data:
        rootnode.data = nodevalue
    else:
        if nodevalue <= rootnode.data:
            if not rootnode.leftchild:
                rootnode.leftchild = BST(nodevalue)
            else:
                insertnode(rootnode.leftchild, nodevalue)
        else:
            if not rootnode.rightchild:
                rootnode.rightchild = BST(nodevalue)
            else:
                insertnode(rootnode.rightchild, nodevalue)
    return 'The node has been successfully inserted'


def preordertraversal(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preordertraversal(rootnode.leftchild)
    preordertraversal(rootnode.rightchild)


def inordertraversal(rootnode):
    if not rootnode:
        return
    inordertraversal(rootnode.leftchild)
    print(rootnode.data)
    inordertraversal(rootnode.rightchild)


def postoredertraversal(rootnode):
    if not rootnode:
        return
    postoredertraversal(rootnode.leftchild)
    postoredertraversal(rootnode.rightchild)
    print(rootnode.data)


def levelordertraversal(rootnode):
    if not rootnode:
        return
    customqueue = Queue()
    customqueue.enqueue(rootnode)
    while not (customqueue.isEmpty()):
        root = customqueue.dequeue()
        print(root.data)
        if root.leftchild:
            customqueue.enqueue(root.leftchild)

        if root.rightchild:
            customqueue.enqueue(root.rightchild)


def searchnode(rootnode, nodevalue):
    if not rootnode:
        print('The value not found')
    else:
        if rootnode.data == nodevalue:
            print('The value has been found')
        elif nodevalue < rootnode.data:
            if not rootnode.leftchild:
                print('The value not found')
            elif rootnode.leftchild.data == nodevalue:
                print('The value has been found')
            else:
                searchnode(rootnode.leftchild, nodevalue)
        else:
            if not rootnode.rightchild:
                print('The value not found')
            elif rootnode.rightchild.data == nodevalue:
                print('The value has been found')
            else:
                searchnode(rootnode.rightchild, nodevalue)


def find_min_value(rootnode):
    if not rootnode:
        return rootnode
    current = rootnode
    while current.leftchild:
        current = current.leftchild
    return current


def deletenode(rootnode, nodevalue):
    if not rootnode:
        return rootnode
    if nodevalue < rootnode.data:
        rootnode.leftchild = deletenode(rootnode.leftchild, nodevalue)
    elif nodevalue > rootnode.data:
        rootnode.rightchild = deletenode(rootnode.rightchild, nodevalue)
    else:
        if not rootnode.leftchild:
            temp = rootnode.rightchild
            rootnode = None
            return temp

        if not rootnode.rightchild:
            temp = rootnode.leftchild
            rootnode = None
            return temp

        temp = find_min_value(rootnode.rightchild)
        rootnode.data = temp.data
        rootnode.rightchild = deletenode(rootnode.rightchild, temp.data)
    return rootnode


def deleteBST(rootnode):
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None
    return 'BST has been successfully deleted'


binarysearchtree = BST(None)
insertnode(binarysearchtree, 70)
insertnode(binarysearchtree, 60)
insertnode(binarysearchtree, 90)
insertnode(binarysearchtree, 50)
insertnode(binarysearchtree, 65)
insertnode(binarysearchtree, 75)
insertnode(binarysearchtree, 100)
insertnode(binarysearchtree, 30)
insertnode(binarysearchtree, 55)
# levelordertraversal(binarysearchtree)
# searchnode(binarysearchtree, 30)
# deletenode(binarysearchtree, 55)
print(deleteBST(binarysearchtree))
levelordertraversal(binarysearchtree)