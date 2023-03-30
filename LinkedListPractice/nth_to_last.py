from LinkedListClass import LinkedList


def find_nth_to_last(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    for _ in range(n):
        if not pointer2:
            return
        pointer2 = pointer2.next
    # print(pointer2)

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    # print(pointer2)
    return pointer1


customll = LinkedList()
customll.generate(10, 0, 99)
print(customll)
print(find_nth_to_last(customll, 5))
