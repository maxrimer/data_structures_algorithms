from LinkedListClass import LinkedList


def removedups(ll):
    if not ll.head:
        return
    else:
        tempnode = ll.head
        tempset = {tempnode.value}
        while tempnode.next:
            if tempnode.next.value in tempset:
                tempnode.next = tempnode.next.next
            else:
                tempset.add(tempnode.next.value)
                tempnode = tempnode.next
        return ll


if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.generate(10, 0, 15)
    print(linkedlist)
    removedups(linkedlist)
    print(linkedlist)


