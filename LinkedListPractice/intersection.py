from LinkedListClass import LinkedList, Node


def intersection(ll1, ll2):
    if ll1.tail is not ll2.tail:
        return False
    else:
        len1 = len(ll1)
        len2 = len(ll2)

        longer = ll2 if len1 < len2 else ll1
        shorter = ll1 if len1 < len2 else ll2

        diff = len(longer) - len(shorter)
        longernode = longer.head
        shorternode = shorter.head

        for _ in range(diff):
            longernode = longernode.next

        while shorternode is not longernode:
            shorternode = shorternode.next
            longernode = longernode.next

    return longernode


# Helper function to place the exact node at the end
def addsamenode(ll1, ll2, value):
    tempnode = Node(value)
    ll1.tail.next = tempnode
    ll1.tail = tempnode
    ll2.tail.next = tempnode
    ll2.tail = tempnode


llA = LinkedList()
llA.generate(5, 0, 10)
llB = LinkedList()
llB.generate(7, 0, 10)

addsamenode(llA, llB, 19)
addsamenode(llA, llB, 16)

print(llA)
print(llB)

print(intersection(llA, llB))