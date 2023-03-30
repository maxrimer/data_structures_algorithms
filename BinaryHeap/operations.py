# common operations on binary heap

class Heap:
    def __init__(self, size):
        self.customlist = (size + 1) * [None]
        self.heapsize = 0
        self.maxsize = size + 1


def peekofheap(rootnode):
    if not rootnode:
        return
    else:
        return rootnode.customlist[1]


def sizeofheap(rootnode):
    if not rootnode:
        return
    else:
        return rootnode.heapsize


def levelordertraverse(rootnode):
    if not rootnode:
        return
    else:
        for i in range(1, rootnode.heapsize + 1):
            print(rootnode.customlist[i])


def heapifytreeinsert(rootnode, index, type):
    if index <= 1:
        return
    parentindex = int(index/2)
    if type == 'Min':
        if rootnode.customlist[index] < rootnode.customlist[parentindex]:
            rootnode.customlist[index], rootnode.customlist[parentindex] = rootnode.customlist[parentindex], rootnode.customlist[index]
        heapifytreeinsert(rootnode, parentindex, type)
    elif type == 'Max':
        if rootnode.customlist[index] > rootnode.customlist[parentindex]:
            rootnode.customlist[index], rootnode.customlist[parentindex] = rootnode.customlist[parentindex], rootnode.customlist[index]
        heapifytreeinsert(rootnode, parentindex, type)


def insertnode(rootnode, nodevalue, heaptype):
    if rootnode.heapsize + 1 == rootnode.maxsize:
        return 'The heap is full'
    rootnode.customlist[rootnode.heapsize + 1] = nodevalue
    rootnode.heapsize += 1
    heapifytreeinsert(rootnode, rootnode.heapsize, type=heaptype)
    return 'The node has been successfully inserted'


def heapifytreeextract(rootnode, index, treetype):
    leftchild = index * 2
    rightchild = index * 2 + 1
    swapchild = None

    if rootnode.heapsize < leftchild:
        return
    elif rootnode.heapsize == leftchild:
        if treetype == 'Min':
            if rootnode.customlist[index] > rootnode.customlist[leftchild]:
                rootnode.customlist[index], rootnode.customlist[leftchild] = rootnode.customlist[leftchild], rootnode.customlist[index]
            return
        else:
            if rootnode.customlist[index] < rootnode.customlist[leftchild]:
                rootnode.customlist[index], rootnode.customlist[leftchild] = rootnode.customlist[leftchild], rootnode.customlist[index]
            return
    else:
        if treetype == 'Min':
            if rootnode.customlist[leftchild] < rootnode.customlist[rightchild]:
                swapchild = leftchild
            else:
                swapchild = rightchild
            if rootnode.customlist[index] > rootnode.customlist[swapchild]:
                rootnode.customlist[index], rootnode.customlist[swapchild] = rootnode.customlist[swapchild], rootnode.customlist[index]
        else:
            if rootnode.customlist[leftchild] > rootnode.customlist[rightchild]:
                swapchild = leftchild
            else:
                swapchild = rightchild
            if rootnode.customlist[index] < rootnode.customlist[swapchild]:
                rootnode.customlist[index], rootnode.customlist[swapchild] = rootnode.customlist[swapchild], rootnode.customlist[index]
        heapifytreeinsert(rootnode, swapchild, treetype)


def extractnode(rootnode, heaptype):
    if rootnode.heapsize == 0:
        return
    delnode = rootnode.customlist[1]
    tempnode = rootnode.customlist[rootnode.heapsize]
    rootnode.customlist[1] = tempnode
    rootnode.customlist[rootnode.heapsize] = None
    rootnode.heapsize -= 1
    heapifytreeextract(rootnode, 1, heaptype)
    return delnode


def deleteentirebh(rootnode):
    rootnode.customlist = None


newbinaryheap = Heap(6)
insertnode(newbinaryheap, 4, 'Max')
insertnode(newbinaryheap, 5, 'Max')
insertnode(newbinaryheap, 2, 'Max')
insertnode(newbinaryheap, 1, 'Max')
insertnode(newbinaryheap, 3, 'Max')
insertnode(newbinaryheap, 7, 'Max')
deleteentirebh(newbinaryheap)
levelordertraverse(newbinaryheap)






