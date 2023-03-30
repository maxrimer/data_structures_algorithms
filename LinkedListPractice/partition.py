from LinkedListClass import LinkedList


def partition(ll, x):
    currnode = ll.head
    ll.tail = ll.head

    while currnode:
        nextnode = currnode.next
        currnode.next = None
        if currnode.value < x:
            currnode.next = ll.head
            ll.head = currnode
        else:
            ll.tail.next = currnode
            ll.tail = currnode
        currnode = nextnode

    if ll.tail.next:
        ll.tail.next = None


customll = LinkedList()
customll.generate(10, 0, 99)
print(customll)
partition(customll, 80)
print(customll)