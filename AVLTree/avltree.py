# operations on avl trees
from create_queue_with_linkedlist import Queue


class AVLTree:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1


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


def postordertraversal(rootnode):
    if not rootnode:
        return
    postordertraversal(rootnode.leftchild)
    postordertraversal(rootnode.rightchild)
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


def searchAVL(rootnode, nodevalue):
    if not rootnode:
        return
    elif rootnode.data == nodevalue:
        print('The value is found')
    else:
        if nodevalue < rootnode.data:
            if rootnode.leftchild.data == nodevalue:
                print('The value is found')
            else:
                searchAVL(rootnode.leftchild, nodevalue)

        if nodevalue > rootnode.data:
            if rootnode.rightchild == nodevalue:
                print('The value is found')
            else:
                searchAVL(rootnode.rightchild, nodevalue)


def getheight(rootnode):
    if not rootnode:
        return 0
    return rootnode.height


def rightrotate(disbalancednode):
    newroot = disbalancednode.leftchild
    disbalancednode.leftchild = disbalancednode.leftchild.rightchild
    newroot.rightchild = disbalancednode
    disbalancednode.height = 1 + max(getheight(disbalancednode.leftchild), getheight(disbalancednode.rightchild))
    newroot.height = 1 + max(getheight(newroot.leftchild), getheight(newroot.rightchild))
    return newroot


def leftrotate(disbalancednode):
    newroot = disbalancednode.rightchild
    disbalancednode.rightchild = disbalancednode.rightchild.leftchild
    newroot.leftchild = disbalancednode
    disbalancednode.height = 1 + max(getheight(disbalancednode.leftchild), getheight(disbalancednode.rightchild))
    newroot.height = 1 + max(getheight(newroot.leftchild), getheight(newroot.rightchild))
    return newroot


def getbalance(rootnode):
    if not rootnode:
        return 0
    return getheight(rootnode.leftchild) - getheight(rootnode.rightchild)


def insertnodeavl(rootnode, nodevalue):
    if not rootnode:
        return AVLTree(nodevalue)

    elif nodevalue < rootnode.data:
        rootnode.leftchild = insertnodeavl(rootnode.leftchild, nodevalue)

    else:
        rootnode.rightchild = insertnodeavl(rootnode.rightchild, nodevalue)

    rootnode.height = 1 + max(getheight(rootnode.leftchild), getheight(rootnode.rightchild))
    balance = getbalance(rootnode)

    if balance > 1 and nodevalue < rootnode.leftchild.data:
        return rightrotate(rootnode)

    if balance > 1 and nodevalue > rootnode.leftchild.data:
        rootnode.leftchild = leftrotate(rootnode.leftchild)
        return rightrotate(rootnode)

    if balance < -1 and nodevalue > rootnode.rightchild.data:
        return leftrotate(rootnode)

    if balance < -1 and nodevalue < rootnode.rightchild.data:
        rootnode.rightchild = rightrotate(rootnode.rightchild)
        return leftrotate(rootnode)
    return rootnode


def getminvalue(rootnode):
    if not rootnode or not rootnode.leftchild:
        return rootnode
    getminvalue(rootnode.leftchild)


def deletenodeavl(rootnode, delnode):
    if not rootnode:
        return rootnode
    elif delnode < rootnode.data:
        rootnode.leftchild = deletenodeavl(rootnode.leftchild, delnode)

    elif delnode > rootnode.data:
        rootnode.rightchild = deletenodeavl(rootnode.rightchild, delnode)

    else:
        if not rootnode.leftchild:
            temp = rootnode.rightchild
            rootnode = None
            return temp

        elif not rootnode.rightchild:
            temp = rootnode.leftchild
            rootnode = None
            return temp

        temp = getminvalue(rootnode.rightchild)
        rootnode.data = temp.data
        rootnode.rightchild = deletenodeavl(rootnode.rightchild, temp.data)
    rootnode.height = 1 + max(getheight(rootnode.leftchild), getheight(rootnode.rightchild))
    balance = getbalance(rootnode)

    if balance > 1 and getbalance(rootnode.leftchild) >= 0:
        return rightrotate(rootnode)
    if balance < -1 and getbalance(rootnode.rightchild) <= 0:
        return leftrotate(rootnode)
    if balance > 1 and getbalance(rootnode.leftchild) < 0:
        rootnode.leftchild = leftrotate(rootnode.leftchild)
        return rightrotate(rootnode)
    if balance < -1 and getbalance(rootnode.rightchild) > 0:
        rootnode.rightchild = rightrotate(rootnode.rightchild)
        return leftrotate(rootnode)
    return rootnode


def deleteentireAVL(rootnode):
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None


newavl = AVLTree(5)
newavl = insertnodeavl(newavl, 10)
newavl = insertnodeavl(newavl, 15)
newavl = insertnodeavl(newavl, 20)
deleteentireAVL(newavl)
levelordertraversal(newavl)























